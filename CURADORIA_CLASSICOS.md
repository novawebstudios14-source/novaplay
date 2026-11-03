# NovaPlay — curadoria de clássicos

Pesquisa de 3 de novembro de 2026. Prioridade: jogos marcantes ou premiados, distinguindo o jogo original da adaptação web. Prêmios só são atribuídos quando confirmados pela organização responsável. Número de títulos não é critério de inclusão.

## Resultado inicial

| Jogo / edição | Projeto e requisitos encontrados | Decisão |
|---|---|---|
| Mario Kart 64 (N64) | [MarioKart64JS](https://github.com/AgentiLoop/MarioKart64JS). Recriação experimental; autor informa pistas, batalha e multiplayer. Canvas preto no navegador remoto, inclusive após Enter. | Adicionado no início do catálogo e no filtro N64, com limitação visível. Corrida não validada. |
| Zelda: Ocarina of Time (N64) | [Clean Room](https://github.com/andrewnakas/oot-cleanroom). Baseado em Ship of Harkinian, com texturas, fontes e sons recriados. Autor informa que não pede ROM ao visitante. Carregador observado; canvas permaneceu escuro. | Adicionado com identificação da build e diferença visual. Partida não validada. O original ganhou [Game of the Year da AIAS em 1999](https://www.interactive.org/awards/award_category_details.asp?idAward=1999&idGameAwardType=65). |
| God of War (PS2, 2005) | [gow-native-pc](https://github.com/Vnnc1/gow-native-pc) é um port nativo para computador e exige uma cópia própria compatível. Não é uma página de jogo pronta para navegador. O original ganhou [Overall Game of the Year da AIAS em 2006](https://www.interactive.org/awards/award_category_details.asp?idAward=2006&idGameAwardType=109). | Prioridade alta, mas não incluir como jogo web pronto. Não confundir com God of War de 2018 nem com as edições de PSP. |
| God of War: Chains of Olympus / Ghost of Sparta (PSP) | [PSP Web Recomp](https://github.com/snuri00/psp-web-recomp) documenta compilação para navegador a partir de imagem de disco própria. O README exige ferramentas de build e descreve limitações, como vídeos pulados. Não fornece um link público pronto com os jogos. | Candidato técnico forte; não cadastrar como “abrir e jogar” antes de encontrar e verificar uma distribuição adequada. Relatos de desempenho do autor não equivalem a testes do NovaPlay. |
| Resident Evil 2 (1998) | [re2-wasm](https://github.com/aarvsn/re2-wasm) descreve um port WebAssembly, com compilação local e arquivos originais fornecidos pelo jogador. Nenhuma partida ou distribuição pública pronta foi validada nesta pesquisa. | Manter na pesquisa; ainda não adicionar ao catálogo principal. |
| Zelda: A Link to the Past (SNES) | [zelda3-web](https://github.com/andrewnakas/zelda3-web) documenta uma build para navegador e extração local a partir de ROM própria. A leitura do README foi feita diretamente na fonte; não foi confirmada uma página pública pronta. | Prioridade alta para a próxima rodada de verificação. |
| Star Fox 64 (N64) | [sf64-cleanroom](https://github.com/andrewnakas/sf64-cleanroom) publica um endereço web, mas descreve texturas e vozes recriadas, inclusive vozes sintetizadas. Não foi testado em partida. | Candidato condicionado à fidelidade e à verificação de jogo. Não anunciar como experiência original intacta. |
| Banjo-Kazooie (N64) | [BanjoRecomp](https://github.com/BanjoRecomp/BanjoRecomp) é um port nativo para Windows/Linux/Mac e requer ROM US 1.0 própria. Um candidato web encontrado no índice retornou 404 na consulta. O original aparece entre os indicados ao prêmio AIAS de 1999. | Continuar pesquisa de versão web; sem inclusão de um link não confirmado. |

## Critérios permanentes

1. Relevância histórica e reconhecimento do título, não tamanho do catálogo.
2. Confirmar a edição: original, remake, demo, mod, recriação ou projeto técnico.
3. Preferir a fonte do criador e documentar os arquivos próprios exigidos.
4. Separar página acessível, launcher observado e partida efetivamente testada.
5. Registrar diferenças de texturas, som, controles, conteúdo e desempenho.
6. Só atribuir um prêmio à edição que realmente o recebeu; não ao port de fãs.

Os jogos já presentes — como GTA, Half-Life, Halo, DOOM, Quake e Tomb Raider — seguem disponíveis. A pesquisa não removeu jogos nem tratou títulos independentes como automaticamente inferiores.

## Segunda rodada — quatro clássicos adicionados

| Título e edição cadastrada | Verificação e decisão |
|---|---|
| [Sonic 3 & Knuckles — A.I.R. Web Beta](https://projects.sappharad.com/s3air_ios/) | Distribuição web de fãs indicada no [site de Sonic 3 A.I.R.](https://sonic3air.org/). O seletor de Sonic_Knuckles_wSonic3.bin foi observado. Adicionado como beta com arquivos próprios obrigatórios; partida não iniciada sem ROM do visitante. |
| [Dune II — OpenDUNE Web](https://dune2js.com/) | Casa Atreides, apresentação e cenário de missão observados. A sessão exibiu conclusão rapidamente; combate, economia e campanha não validados. Adicionado com teste limitado. |
| [PAC-MAN — Google Doodle de 2010](https://doodles.google/doodle/30th-anniversary-of-pac-man/?hl=pt-BR) | Insert Coin iniciou o labirinto; comandos nas setas, personagens e pontuação de 10 foram observados. Adicionado como edição comemorativa, sem confundir com a ROM original do arcade. Sessão curta, sem validar todas as fases. |
| [Tetris — Marathon oficial](https://play.tetris.com/games/) | Link de jogo obtido no catálogo oficial. O player informou que WebGL não está disponível no navegador remoto. Adicionado como edição web oficial atual, com limitação explícita; não confundir com versões de NES/Game Boy. |

### Candidatos que não passaram para o catálogo nesta rodada

- Pokémon Emerald: o [projeto WebAssembly](https://github.com/tripplyons/pokeemerald-wasm) existe, mas a página de jogo encontrada retornou erro de conexão neste navegador. Não foi adicionada uma entrada com partida presumida.
- Jazz Jackrabbit: a página web indicada pelo [fork OpenJazz](https://github.com/midzer/openjazz) retornou 404 na consulta.
- Fallout: os projetos consultados descrevem uso de dados próprios e builds nativas; não foi confirmada uma distribuição web pronta nesta rodada. Permanece prioridade de pesquisa, sem trocar o original por uma recriação não identificada.
- Heroes of Might and Magic III: o [fork WebAssembly do VCMI](https://github.com/realkompot/vcmi_wasm_demo/tree/wasm-demo) se descreve como demonstração técnica, com conexão cliente/servidor problemática e build não totalmente automatizada. A página hospedada encontrada na DOS Zone não pôde ser validada na conexão atual.
- Warcraft II, Age of Empires e Aladdin: há páginas no catálogo da DOS Zone, mas os acessos diretos retornaram timeout/erro de conexão nesta rodada. Não foram cadastrados como jogos verificados.
- [Command & Conquer HTML5](https://adityaravishankar.github.io/command-and-conquer/): a página do autor descreve uma prova de conceito, distinta do jogo completo, e aponta URLs legadas. Não entrou como edição original completa.
- Sonic Mania: o repositório encontrado não bastou para confirmar uma distribuição web atual e estável. Não foi promovido ao catálogo só por estar em um índice.

A seleção desta rodada se baseia em relevância histórica e identificação das edições. Não se atribuiu prêmio específico a esses quatro jogos sem confirmação na fonte da premiação.


## Ajuste solicitado em 03/11/2026
PAC-MAN e Tetris removidos do catálogo ativo a pedido do usuário. Total atual: 104 entradas. Jogos com arquivos próprios recebem selo, aviso antes de abrir e fontes por edição. Half-Life/CS: compra Steam e guia WebXash; Halo: XISO de disco Xbox próprio; CTR: disco original PS1; Sonic A.I.R.: arquivo compatível da edição antiga citada pelo autor, sem promessa de compra disponível.
