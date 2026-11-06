# Bomba Patch para navegador — investigação técnica

Data: 2026-11-06

## Estado
Pesquisa de bases concluída. Nenhum executável do jogo foi analisado, recompilado ou testado.
Não há versão jogável criada nem nova entrada adicionada ao catálogo.
Falta a imagem de disco da edição exata a analisar. O nome "Bomba Patch" não identifica
um único binário: a análise precisa registrar edição, plataforma, executável e hashes.

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
