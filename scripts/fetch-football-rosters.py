#!/usr/bin/env python3
"""Capture ESPN roster responses for investigation; does not modify game data."""
import argparse
import concurrent.futures
import datetime
import hashlib
import json
import pathlib
import urllib.request


def fetch(url):
    request = urllib.request.Request(url, headers={"User-Agent": "NovaPlay-Research/1.0"})
    with urllib.request.urlopen(request, timeout=45) as response:
        data = json.load(response)
    return {"source_url": url, "fetched_at": datetime.datetime.now(datetime.timezone.utc).isoformat(), "response": data}


def compact(snapshot):
    """Keep factual roster fields; omit ratings, images and unrelated API payloads."""
    teams = snapshot["teams"]
    entries = teams["response"]["sports"][0]["leagues"][0]["teams"]
    teams["response"] = [{key: entry["team"].get(key) for key in
                          ("id", "displayName", "abbreviation", "color", "alternateColor")}
                         for entry in entries]
    for roster in snapshot["rosters"]:
        raw = roster.pop("response")
        roster["response_json_sha256"] = hashlib.sha256(
            json.dumps(raw, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
        roster["season_reported"] = raw.get("season")
        roster["athletes"] = [{key: athlete.get(key) for key in
                               ("id", "displayName", "jersey", "position", "dateOfBirth", "height", "weight")}
                              for athlete in raw["athletes"]]
    return snapshot


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--league", choices=["bra.1", "bra.2"], default="bra.1")
    parser.add_argument("--season", type=int, required=True)
    parser.add_argument("--out", type=pathlib.Path, required=True)
    args = parser.parse_args()
    base = f"https://site.api.espn.com/apis/site/v2/sports/soccer/{args.league}"
    teams = fetch(f"{base}/teams?season={args.season}&limit=100")
    entries = teams["response"]["sports"][0]["leagues"][0]["teams"]
    ids = [str(entry["team"]["id"]) for entry in entries]
    if not ids or len(set(ids)) != len(ids):
        raise ValueError("Empty team list or duplicated team identifiers")
    def roster(team_id):
        result = fetch(f"{base}/teams/{team_id}/roster?season={args.season}")
        if not result["response"].get("athletes"):
            raise ValueError(f"No athletes returned for {team_id}")
        result["team_id"] = team_id
        return result
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        rosters = list(pool.map(roster, ids))
    snapshot = {"requested_season": args.season, "league": args.league,
                "status": "source_snapshot_not_applied_to_game",
                "limitations": ["Season is a request parameter, not independent proof of historical accuracy.",
                                "No game skill ratings inferred; no player identity or transfer independently verified."],
                "teams": teams, "rosters": rosters}
    encoded = (json.dumps(compact(snapshot), ensure_ascii=False, indent=2) + "\n").encode()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    # Exclusive creation prevents accidental replacement of an earlier snapshot.
    with args.out.open("xb") as output:
        output.write(encoded)
    print(json.dumps({"file": str(args.out), "teams": len(ids), "rosters": len(rosters),
                      "sha256": hashlib.sha256(encoded).hexdigest()}))


if __name__ == "__main__":
    main()
