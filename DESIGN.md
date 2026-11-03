# NOVA PLAY — design contract

The portal helps Brazilian players discover browser-game projects, understand requirements and open a suitable destination. Keep the existing buildless HTML/CSS/JS stack.

## Confirmed data
76 selected entries, 13 categories. Research: 954 index records, 134 destination checks, 125 HTTP successes. HTTP success is not proof of gameplay. Current evidence is dated 2026-11-03; no background checking or automatic verification is claimed.

## Visual decisions
Content first: game imagery, concise editorial summaries, a recognizable title and a clear external-launch action. Use publisher images only to identify the original title, with source attribution and an explicit distinction from the community port. Typographic fallback for entries without suitable images. No fabricated ratings, popularity, online counts or playtime.

Palette: background #07090f; surface #111726; text #f2f5ff; secondary #9caac5; accent #386dff with purple #9b65ff. Space Grotesk for headings; DM Sans for interface text. Body copy 13–15px; primary controls at least 44px; mobile navigation has visible labels. Grid: 4 columns desktop, 3 medium, 2 narrow. Category strip scrolls horizontally; advanced filters expand inline.

## Interaction contract
Cards use real links, with separate favorite buttons. Every game has a generated static /jogos/<slug>/ page. Filters/search/order are URL state. Back preserves the previous catalog URL. Favorites and opened destinations stay browser-local and can be exported/imported with validation. Recommendations use shared category, not a fabricated recommendation engine. Random selection respects filters. External launch is stated before the action.

## Quality gates
Keyboard focus, skip link, native dialog behavior, reduced motion, explicit image dimensions, lazy loading for catalog imagery, responsive layout down to 320px, text overflow, empty states and malformed import handling. Feature detection must never imply full game compatibility.

## Reference decisions
Steam: discovery/favorites; itch.io: controls and input filters; Poki/CrazyGames: fast browsing and intent-based collections. Engineering references: Addy Osmani frontend-ui-engineering and Vercel Web Interface Guidelines. These guide implementation, without copying branding or product claims.

## Explicit visual preference
The user rejects whitish and washed-out palettes. Use deep black/navy surfaces and saturated blue/purple accents. Never reintroduce pastel lime, pale panels, or a whitening hero overlay. Keep light text for readability. The homepage cycles through seven sourced game highlights, with visible controls and pause support. Every catalog entry must have locally stored, attributed game or project artwork.

Homepage hero must keep a fixed height at each breakpoint across every slide. Show only the category, game title, primary links and dot indicators. No arrows, pause button, editorial counter, duplicate title, promotional paragraph or verification copy in the hero; detailed evidence stays on the game page.

Restore the editorial headline, game name and concise description in the fixed-height hero per latest user preference. Keep only dot controls. The brand icon is a gamepad, not an N monogram.

## 2026-11-03 visual refresh
Immersive dark arcade direction: a larger fixed-height hero, blue-to-purple primary actions, an image-led spotlight rail, photographic collection tiles and framed game cards. Preserve existing links, local library data and evidence descriptions. References reviewed: Steam (https://store.steampowered.com/), Xbox Game Pass (https://www.xbox.com/pt-BR/xbox-game-pass), Poki (https://poki.com/br), CrazyGames (https://www.crazygames.com/br/). These inform hierarchy and browsing patterns, without copying branding.

## Catalog expansion
100 entries: 24 additional creator-hosted browser games, demos and original web releases. Added Puzzle and Ritmo categories plus a Navegador platform group. New entries record HTTP success only, without claiming tested gameplay.
