# SASSE Core

Projeto autoral de arquitetura de sistemas focado em execução controlada, validação de instruções e organização por camadas.

## Visão geral

A SASSE explora uma estrutura onde:

- instruções não são executadas automaticamente
- a validação antecede a execução
- o sistema registra estado e histórico
- há separação entre julgamento lógico e processamento

## Estrutura do repositório

- `SDB-Corpus` → regras, princípios e validação
- `Runtime-PAI` → processamento lógico
- `Kernel-Rust` → execução
- `MSPB-Trace` → rastreabilidade e histórico
- `Semantic-Graph` → organização semântica
- `Hologram-Veu` → interface e manifestação

## Arquitetura

Veja o arquivo [`ARCHITECTURE.md`](./ARCHITECTURE.md) para uma visão geral da organização do sistema.

## Status

Em desenvolvimento.
Estrutura inicial pública organizada no GitHub.
