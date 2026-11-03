# NOVA PLAY

Portal de jogos de navegador com 104 títulos, capas locais, busca, filtros, favoritos e carrossel.

Site: https://novaplay-arcade.talita-marques-924.chatgpt.site/

## Executar localmente

Requer Python 3 para o servidor e Node.js para regenerar páginas.

```sh
python3 -m http.server 8080 --directory dist
```

Abra http://localhost:8080. Não precisa instalar dependências.

## Estrutura

- `dist/`: site pronto para hospedagem estática, incluindo imagens e páginas de cada jogo.
- `dist/games.js`: catálogo e fontes das imagens.
- `scripts/build-pages.mjs`: gera as páginas individuais após alterações no HTML ou catálogo.
- `DESIGN.md`: diretrizes visuais.

Depois de editar:

```sh
node scripts/build-pages.mjs
node --check dist/app.js
node --check dist/games.js
```

Hospede a pasta `dist`. Os jogos abrem em projetos externos; requisitos e resultados de verificação estão nas fichas. HTTP 200 não confirma uma partida funcionando. Jogos, marcas e artes pertencem aos respectivos titulares; as fontes estão registradas em `dist/assets/sources.json`.
