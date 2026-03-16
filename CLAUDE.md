# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Visão Geral

Repositório Python em estágio inicial de desenvolvimento, localizado em ambiente Windows com VS Code.

## Idioma

Sempre responder em **português brasileiro (pt-BR)**. Quando houver conteúdo técnico em inglês (mensagens de erro, comentários de código, documentação), exibir a versão original e logo abaixo a tradução em português entre parênteses.

Exemplo:
- `File not found` (Arquivo não encontrado)
- `git: command not found` (git: comando não encontrado)

## Ambiente

- **Plataforma:** Windows 11
- **Shell:** bash (Git Bash)
- **Editor:** Visual Studio Code
- **Linguagem:** Python

## GitHub

- **Repositório:** https://github.com/borgesrodri4-bot/claudepy
- **Conta:** borgesrodri4-bot
- **Branch principal:** master

### Auto-push configurado

A cada `git commit`, o projeto é enviado automaticamente ao GitHub via hook `post-commit` (`.git/hooks/post-commit`).

Para commitar e enviar alterações:

```bash
git add .
git commit -m "mensagem do commit"
# o push acontece automaticamente após o commit
```

(`git add .` — adiciona todos os arquivos modificados)
(`git commit -m "..."` — salva as alterações com uma mensagem)
(o push para o GitHub ocorre automaticamente)
