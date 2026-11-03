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

## Terceira rodada — distribuições prontas verificadas

Rodada de 3 de novembro de 2026: quatro clássicos adicionados, elevando o catálogo de 104 para 108 entradas. O foco foi relevância histórica e identificação da edição. Nenhum prêmio novo foi atribuído sem consulta à organização responsável. PAC-MAN e Tetris continuam fora do catálogo ativo.

| Título / edição | Fonte do criador e arquivos | Resultado observado e decisão |
|---|---|---|
| Jazz Jackrabbit (1994) — OpenJazz Shareware | [Motor OpenJazz](https://github.com/AlisterT/openjazz) e [distribuição web](https://github.com/openjazz/openjazz.github.io). O README da distribuição identifica dados shareware 1.1 e Holiday Hare. | [Página pronta](https://openjazz.github.io/) respondeu HTTP 200; apresentação, menu “THIS IS SHAREWARE” e instruções observados. Movimento em fase não validado. Adicionado como shareware, não como edição comercial completa. Este endereço indicado pelo mantenedor difere do link do fork que retornou 404 na rodada anterior. |
| Flashback (1992) — demo DOS em TypeScript | [Flashback Web](https://github.com/warpdesign/flashback-web), reescrita baseada em REminiscence. [Demo pública](https://warpdesign.github.io/flashback-web/) carregada sem arquivos do visitante; teclado obrigatório. | HTTP 200; Play acionado e introdução Delphine Software / US Gold renderizada. Tab enviado; controle de Conrad e progressão não validados. Apenas demo DOS; sem saves, joystick, toque ou importação da edição completa; opcodes e áudio têm limitações documentadas. |
| Another World (1991) — demo DOS HTML5 | [another_js](https://github.com/cyxx/another_js), [demo pública](https://cyxx.github.io/another_js/). Dados de demonstração já carregados; código arquivado pelo autor. | HTTP 200; apresentação, seletor Introduction/Water e cenário Water renderizados. Seta enviada, mas resposta do personagem e progressão não validadas. Ausência de música/efeitos declarada pelo autor; não apresentar como remaster ou jogo completo. |
| Heroes of Might and Magic II (1996) — fheroes2 1.1.17 Web | [Port e requisitos](https://github.com/Carter54git/fheroes-1.1.17-ported-to-web), [launcher indicado pelo autor](https://buildenginegames.online/homm2webgit/index.html). Exige DATA/HEROES2.AGG e MAPS/ da cópia própria; expansão, música e vídeos dependem de arquivos adicionais. | HTTP 200; seletor de pasta/ZIP renderizado, Click to Play desabilitado sem dados. Nenhum arquivo original fornecido, nenhuma partida iniciada. Adicionado com selo e aviso de arquivos obrigatórios, guia do autor e motor como fontes. Não confundir este motor com o executável original ou prometer todas as edições compatíveis. |

As quatro adições têm imagens publicadas pelos respectivos projetos, armazenadas localmente e atribuídas em `dist/assets/sources.json`. As imagens identificam o projeto e não substituem a evidência de teste. God of War, Resident Evil 2, Banjo-Kazooie e os outros candidatos técnicos mantêm as decisões anteriores; não foram promovidos por quantidade nem por existir apenas um repositório.

## Quarta rodada — exigência de partida controlável

Pedido: incluir Mortal Kombat, UFC, NBA 2K, God of War, Call of Duty e Assassin’s Creed, garantindo funcionamento. Para esta rodada, uma nova entrada só seria aceita após iniciar uma partida e observar resposta direta aos controles. Menu, vídeo, HTTP 200, luta sem resposta comprovada ou relato de outro índice não bastam. O teste foi feito no Chromium remoto disponível e não garante todos os aparelhos. **Resultado: zero novas entradas ativas; total mantido em 108.**

| Candidato / edição | Resultado observado em 03/11/2026 | Decisão |
|---|---|---|
| Mortal Kombat DOS — DOS.Zone | [Página](https://dos.zone/mortal-kombat-1993/) apresentou erro de conexão/timeout, inclusive após uma recarga. | Não incluir como funcional. |
| Mortal Kombat II — demo DOS | [DOSGames](https://dosgames.com/game/mortal-kombat-2/) iniciou DOSBox, apresentação, seleção de Liu Kang por F1/Enter e luta contra Reptile com cronômetro, dano e rounds. Setas e F10 enviados, mas resposta direta de movimento/ataque não comprovada. A página identifica demo limitada a Liu Kang/Reptile. | Evidência parcial, não passa no critério estrito de controles. Sem entrada ativa nova. |
| Mortal Kombat 9 — projeto de fãs | [Launcher](https://mk9.lauta.site/) desabilitou Play por ausência de WebGPU/aceleração gráfica no navegador de teste. | Não incluir como funcional; limitação do ambiente, não afirmação de falha universal. |
| UFC Throwdown — candidato PS2 | [Endereço anteriormente citado](https://ufc2.online/) redireciona para `/lander`, domínio estacionado GoDaddy com anúncios e “Adquira este domínio”. | Não incluir. Não confundir Throwdown com UFC moderno. |
| NBA 2K12 — candidato PS2 | [Endereço anteriormente citado](https://nba2k12.online/) redireciona para `/lander`, domínio estacionado GoDaddy. | Não incluir; descrições anteriores de agregadores não refletem o estado atual. |
| God of War: Chains of Olympus / Ghost of Sparta — PSP | [Chains](https://godofwarchains.online/) e [Sparta](https://godofwarsparta.online/) redirecionaram para páginas GoDaddy `/lander`, sem jogos. | Não incluir. |
| God of War II — PS2 Web Recomp | [Repositório](https://github.com/snuri00/ps2-web-recomp) exige compilação e disco próprio. Nenhuma distribuição pronta ou combate validado nesta rodada. | Pesquisa técnica, sem promessa de abrir e jogar. |
| Black Ops Zombies — registro existente | [Projeto](https://vel.gg/bsz): Single Player / Classic guns / Low e Kino der Toten selecionados. O carregamento mostrou “UNSUPPORTED GRAPHICS — WebGL2 is unavailable”. | Registro preservado; ficha atualizada como teste limitado por WebGL2. Não é prova de falha em PCs com suporte. |
| Modern Warfare — Open Victor Zulu, registro existente | [Projeto](https://ovz-game-production.up.railway.app/) informa que está offline após um pedido de DMCA. | Registro preservado com indisponibilidade visível; abertura para jogar desativada. |
| Call of Duty Web Collection | [Página candidata](https://cod-webports.pages.dev/) escura, sem controles ou partida observável. | Não incluir. |
| Assassin’s Creed: Freerunners — spin-off Ubisoft Nano | [Serviço do criador](https://nano.ubisoft.com/) apresentou erro de conexão upstream. [Ubisoft](https://news.ubisoft.com/en-us/article/7xfneqJoWr5BvNVp6dyuFQ/ubisoft-nano-squeezing-big-games-into-small-spaces) identifica-o como arcade runner no universo da série, não adaptação dos jogos principais. | Sem partida testada, não incluir nem usar como substituto silencioso de Assassin’s Creed principal. |
| Assassin’s Creed principal | Não foi encontrada distribuição pública pronta com partida controlável verificável; resultados de port nativo/runtimes exigindo arquivos próprios não constituem jogo web confirmado. | Continuar pesquisa. |

As entradas históricas e experimentais já existentes não foram removidas em bloco. Sua documentação de limitações continua válida. A revisão corrigiu especificamente os dois Call of Duty testados e preservou a exclusão de PAC-MAN/Tetris. Nenhum jogo, ROM ou ISO foi adquirido, importado ou redistribuído para tentar contornar os requisitos.
