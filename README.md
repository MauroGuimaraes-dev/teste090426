# ComboMulti_R2 — fonte original e backup no monorepo

## Fonte original (código executado pelo Agent)

A fonte original deste robô fica no repositório:

`C:\Rpa\MauroGuimaraes-dev\ComboMulti_R2`

Esse repositório é o que deve ser publicado no remoto (GitHub/GitLab) usado no cadastro do robô no Orquestrador.
O Agent sempre executa o código vindo da URL Git cadastrada em `TB_ROBOTS` (`gitlab_repo_url`), via `git clone`.

## Pasta no monorepo (`robos/ComboMulti_R2`)

Esta pasta no OrquestradorClaro (`robos/ComboMulti_R2/`) é apenas um **backup versionado** (espelho de referência) para histórico e documentação.

Ela **não é** a fonte primária de execução do Agent.

## Fluxo recomendado

1. Editar e validar primeiro em `C:\Rpa\MauroGuimaraes-dev\ComboMulti_R2`.
2. Fazer commit/push no repositório remoto oficial do robô.
3. Copiar para `robos/ComboMulti_R2/` no monorepo apenas para manter o backup commitado alinhado.

## Cópia em `examples/`

`examples/robo-claro-playwright/` mantém uma versão espelho para roteiro/template técnico.
