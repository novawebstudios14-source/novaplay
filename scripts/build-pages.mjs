import fs from 'node:fs';
import vm from 'node:vm';
const html = fs.readFileSync('dist/index.html', 'utf8');
const games = vm.runInNewContext(fs.readFileSync('dist/games.js', 'utf8') + ';games');
const esc = s => String(s).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
for (const g of games) {
  const page = html.replace(/<title>.*?<\/title>/, `<title>${esc(g.name)} — NOVA PLAY</title>`)
    .replace(/(<meta name="description" content=")[^"]*/, `$1${esc(g.summary || g.desc)}`)
    .replace(/(<meta property="og:title" content=")[^"]*/, `$1${esc(g.name)} — NOVA PLAY`);
  fs.mkdirSync(`dist/jogos/${g.slug}`, {recursive: true});
  fs.writeFileSync(`dist/jogos/${g.slug}/index.html`, page);
}
fs.writeFileSync('dist/404.html', html);
console.log(`Generated ${games.length} game pages and fallback.`);
