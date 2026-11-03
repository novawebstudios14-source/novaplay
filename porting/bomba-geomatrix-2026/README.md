# Bomba Patch — perfil experimental de port web

Objetivo: adaptar o próprio jogo para navegador, preservando a experiência original. Este diretório contém scripts e correções da ferramenta; não contém ISO, executável comercial, código traduzido do jogo ou build jogável.

## Estado verificado

- Edição examinada: Bomba Patch GeoMatrix, outubro de 2026, PlayStation 2.
- ISO examinada: 2.572.746.752 bytes; BOOT2 `cdrom0:\BPGE_010.26;1`, modo NTSC.
- SHA-256 do executável de referência: `0236a6970622d0ba7c0f180de523403cc571fbf3f402e9f0d9f8cb77e77c7abd`.
- CRC informado pelo portador: `3EAACE68`.
- Ferramenta: https://github.com/snuri00/ps2-web-recomp, revisão `e026b971324068773eed88bf502437de9e581b6b`.
- Compiladores de EE e VU construídos. Três regressões upstream passaram. Comparações vetoriais: 400.000 casos passaram. Carregador ELF: BSS com offset além do EOF e reserva vazia fora da RAM testados; dados inválidos rejeitados.
- O teste nativo chegou à tela em português de cartão de memória, aos 900 frames. Até a quinta rodada foram observados trechos de código dinâmico ausentes; a última parada registrada foi `0x008D5C70`, aos 934 frames.
- **Menu principal, partida e build web ainda não validados. Não existe publicação jogável concluída.**

O ambiente temporário reiniciou durante a continuação. Estes arquivos preservam as correções e o procedimento para reconstrução. Não alteram o catálogo público.

## Construção local

Requer Git, Python 3, CMake, Ninja e um compilador C++20. GCC 13 com `<format>` pode construir as ferramentas; para o runner, prefira Clang por causa de `musttail`. O Clang incluído no Emscripten também foi usado nos testes.

1. Prepare a revisão upstream acima e aplique `runtime-fixes.patch`.
2. Copie `entry-hints.py` para `scripts/novaplay_hints.py` da ferramenta.
3. Use a ISO de uma cópia própria com o executável esperado.
4. Rode `build-local.sh /caminho/ps2-web-recomp /caminho/jogo.iso`.
5. Examine `games/bomba-geomatrix-2026/explore.log` e os frames. Uma compilação concluída **não** confirma que o jogo funcione. Só avance ao navegador após verificar o resultado do runner.

Distribuição da ferramenta e distribuição do conteúdo do jogo são coisas diferentes. Preserve a licença e os créditos upstream. Não atribua a criação original de Bomba Patch ao NovaPlay.
