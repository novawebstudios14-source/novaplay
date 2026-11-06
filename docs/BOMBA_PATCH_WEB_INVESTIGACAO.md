# Bomba Patch para navegador — investigação técnica

Data: 2026-11-06

## Estado
Pesquisa de bases e compilação do recompilador realizadas. Nenhum executável do jogo foi analisado, recompilado ou testado.
Não há versão jogável criada nem nova entrada adicionada ao catálogo.
Falta a imagem de disco da edição exata a analisar. O nome "Bomba Patch" não identifica
um único binário: a análise precisa registrar edição, plataforma, executável e hashes.

## Avanço verificado em 06/11/2026
- Código de ps2-web-recomp baixado no commit e026b971324068773eed88bf502437de9e581b6b.
- Compilado o alvo eerecomp com GCC 13.3.0 e CMake 4.4.4.
- Passaram os testes upstream analysis_tailcall.py, elf_bss.py e codegen_fallthrough.py.
  GCC emitiu avisos sobre o atributo clang::musttail no último teste, que encerrou com código 0.
  São regressões sintéticas do recompilador, não testes de compatibilidade do jogo.
- Não foram compilados o runtime completo, Emscripten ou um jogo para navegador.
- Coletados 20 clubes e 20 respostas de elenco da ESPN, totalizando 944 registros de atletas.
  Isso não significa 944 jogadores únicos, inscritos ou confirmados no elenco atual.
  As 20 respostas identificam a temporada 2026. Snapshot:
  research/football/bra-1-2026-2026-11-06.json.
- O script scripts/fetch-football-rosters.py reproduz a coleta, conserva URL e horário,
  resume campos factuais e não calcula atributos de jogo. Não foi aplicado à ISO.

## Localização dos arquivos do jogo
- O perfil https://linktr.ee/bombapatchgeomatrix aponta para https://superbombapatch.com/.
- A página https://superbombapatch.com/products/super-bomba-patch-ps2 anuncia
  Super Bomba Patch 2027 (PS2), a partir de R$ 23,90, com entrega digital por e-mail
  após a compra. Não foi realizada compra nem recebido arquivo.
- https://mymaxandroidpsp.com/2026/05/01/novo-bomba-patch-2026-ps2-iso-download-100-atualizado-opl-pcsx2-android/
  liga a uma pasta MediaFire, o1ftln00w9px8. A extração web não forneceu arquivos
  utilizáveis; uma tentativa de listar a pasta pela API não retornou JSON válido.
  Isso não comprova que a pasta esteja vazia para todos os usuários.
- https://baixapatch.com/2026/10/26/bomba-patch-2027-brasileirao-100-atualizado/
  anuncia edição Maymax de outubro, mas a extração consultada não forneceu ISO.
- Outras páginas indexadas anunciam ISOs; anúncio não equivale a bytes obtidos,
  autenticidade, integridade ou permissão de redistribuição.
- Resultado desta etapa: nenhuma ISO foi baixada; nenhum hash de disco foi verificado.

## Outras ferramentas localizadas
- https://github.com/hiitsgabe/retro_roster_patcher — referência MIT para atualização
  de elencos; inclui PES 2013 PS2 e WE2002 PS1, não suporte declarado a WE10 PS2.
  Código consultado no commit 1e0ec83968bd8de2f1882856a4baed49e9d020b2.
- https://github.com/moth1995/AFS_PES_PSP_Converter — MIT, conversor de AFS de
  PES 2010 PSP. Não presumir compatibilidade com AFS de WE10 PS2.
- https://github.com/dzakyraf/pes2017-recomp — referência de recompilação de PES2017
  Xbox360 para Android ARM64; não é um port pronto para navegador.
- https://zenhax.com/viewtopic.php@t=2569.html — discussão técnica de extração WE10
  com relatos de formatos diferentes entre arquivos AFS; exige inspeção de cada formato.

## Reproduzir a verificação já realizada

    git clone https://github.com/snuri00/ps2-web-recomp.git
    cd ps2-web-recomp
    git checkout e026b971324068773eed88bf502437de9e581b6b
    cmake -S . -B build/tools -DCMAKE_BUILD_TYPE=Release
    cmake --build build/tools --target eerecomp -j 2
    python3 tests/analysis_tailcall.py
    python3 tests/elf_bss.py
    python3 tests/codegen_fallthrough.py

Coleta dos dados, a partir da raiz da Nova Play (o destino deve ser novo):

    python3 scripts/fetch-football-rosters.py --season 2026 --out research/football/nova-coleta.json

## Bases verificadas
- https://github.com/jpd002/Play- — emulador PS2 com versão web.
- https://github.com/jpd002/Play-Compatibility/issues/988 — Winning Eleven 10,
  SLPM-66374, marcado state-ingame. Relato de 24/08/2019 menciona problemas de som,
  texturas e lentidão em partida. Não prova o estado da versão atual nem do patch.
- https://github.com/snuri00/ps2-web-recomp — recompilação do executável PS2
  para C++/WebAssembly com runtime. README documenta Gran Turismo 4 e God of War II;
  não fornece validação de Winning Eleven/Bomba Patch.
- https://github.com/PeterC10/PESEditor — editor de option files PES6. O arquivo
  src/editor/OptionFile.java documenta estruturas, blocos e contêineres de saves.
  Compatibilidade com a edição alvo precisa ser comprovada antes de reutilizar offsets.
- https://github.com/nthachus/pes-editor — editor de option files PES2014 PS2;
  referência de outra versão, não substituto direto do formato WE10.

## Hipótese de implementação
Testar primeiro o disco exato em Play!.js para obter uma referência de execução.
Em paralelo técnico posterior, tentar PS2 Web Recomp e investigar os erros encontrados.
Atualizar elencos, uniformes e bancos de dados é uma etapa separada do port.
Não inventar transferências, estatísticas, offsets de arquivos ou compatibilidade.
Não usar plugins ASI de PES para Windows como se fossem binários PS2.

## Entrada necessária
Imagem de disco própria/autorizada do jogo-base ou da edição do patch escolhida.
Option file e patch separados, se disponíveis, com versão e origem.
Registrar SHA-256 da ISO e do executável indicado em SYSTEM.CNF antes de alterar dados.
Manter uma cópia intacta e trabalhar em cópia.

## Experimento de recompilação
Comandos documentados pelo upstream, ainda não executados para este jogo:

    git clone https://github.com/snuri00/ps2-web-recomp.git
    cd ps2-web-recomp
    scripts/port.sh nova-futebol "/caminho/jogo.iso"
    python3 scripts/serve.py build/web-nova-futebol games/nova-futebol/disc.iso

Fixar o commit utilizado antes da compilação. Examinar os logs e as capturas
games/nova-futebol/shots. Chegar ao menu não comprova partida funcionando.

## Critérios de aceitação
1. Identificar disco, região, executável e formatos dos arquivos de dados.
2. Iniciar partida e concluir uma partida, verificando áudio, renderização e controles.
3. Validar save e recarregamento, teclado e controle; testar toque em aparelho real.
4. Registrar navegador, aparelho e desempenho observado, sem extrapolar para outros dispositivos.
5. Aplicar uma alteração pequena de dados, conferir no jogo e validar integridade do save.
6. Atualizar os dados da temporada escolhida com fontes e data de corte.
7. Integrar à Nova Play apenas com estado de compatibilidade e requisitos comprovados.

## Hospedagem
O runtime de recompilação usa WebGPU e SharedArrayBuffer; documenta isolamento com
Cross-Origin-Opener-Policy: same-origin e Cross-Origin-Embedder-Policy: require-corp,
além de leitura do disco por HTTP Range. Avaliar origem separada para não alterar
os recursos externos do catálogo existente. Compatibilidade no iPhone não foi testada.

O upstream não inclui os dados do jogo e orienta manter os binários recompilados
localmente. Para publicação pública, definir previamente quais dados e derivados
podem ser distribuídos; um carregador de arquivo local evita hospedar a ISO.

## Nova tentativa de obtenção — 06/11/2026
- Localizado o site MyMaxFF em https://mymaxff.tgamesandroid.com/.
- A publicação de 21/10/2026
  https://mymaxff.tgamesandroid.com/2026/10/download-da-iso-bomba-patch-2027-completa-com-todas-narracoes-ps2-opl-pcsx2-100-atualizado.html/
  contém um botão com destino literal COLOQUE_AQUI_O_LINK_DA_ISO, que retornou 404.
  A opção de câmera PS4 leva a uma pasta MediaFire, não a um arquivo identificado.
- A publicação https://mymaxff.tgamesandroid.com/2026/07/6787.html/
  forneceu arquivos específicos:
  - Cazé TV: https://www.mediafire.com/file/xo5du8s2b4t3dq5/BOMBA_PATCH_PS2__MYMAX_CAZE_TV.rar/file
    — página informa 902,44 MB e upload de 13/07/2026.
  - André Henning: https://www.mediafire.com/file/psn0m3otfezsp36/BOMBA_PATCH_PS2__MYMAX_ANDRE_HENNING.rar/file
    — página informa 923,83 MB e upload de 13/07/2026.
  - Cléber Machado: https://www.mediafire.com/file/n5yj8kb0gyhfkes/BOMBA_PATCH_PS2__MYMAX_CLEBER_MACHADO.rar/file
    — página informa 1,14 GB e upload de 13/07/2026.
- O acesso ao download Cazé TV pela busca redirecionou à reparação do MediaFire.
  Nos outros dois, a ferramenta de busca chegou a uma resposta application/x-rar,
  mas não aceita esse tipo de conteúdo para obtenção dos bytes.
- Tentativas de leitura limitada pelo executor dos links Cazé TV e André Henning
  retornaram HTTP 206 com 195 bytes de HTML: Site Unavailable / Unable to access this site.
  Não continham assinatura RAR. O status HTTP sozinho não confirma o download.
- Não é correto declarar esses links mortos ou os arquivos íntegros:
  a origem apresentou os arquivos, mas este ambiente não obteve os bytes.
  Nenhum arquivo foi executado, extraído ou publicado. Nenhuma nova compilação
  do jogo foi possível; os testes anteriores continuam sendo apenas da ferramenta.
