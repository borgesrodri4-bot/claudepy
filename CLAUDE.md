# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## Visão Geral

Repositório de scripts Python e recursos de desenvolvimento, localizado em ambiente Windows com VS Code. Funciona também como **hub de prompts, skills e referências** para outros projetos gerenciados por este usuário.

---

## Idioma

Sempre responder em **português brasileiro (pt-BR)**. Quando houver conteúdo técnico em inglês (mensagens de erro, comentários de código, documentação), exibir a versão original e logo abaixo a tradução em português entre parênteses.

Exemplo:
- `File not found` (Arquivo não encontrado)
- `git: command not found` (git: comando não encontrado)

---

## Ambiente

- **Plataforma:** Windows 11 Home Single Language
- **Shell:** bash (Git Bash)
- **Editor:** Visual Studio Code com extensão Claude Code
- **Linguagem principal:** Python
- **Node/Next.js:** disponível (usado no projeto agencia-esteira)

---

## GitHub

- **Repositório:** https://github.com/borgesrodri4-bot/claudepy
- **Conta:** borgesrodri4-bot
- **Branch principal:** master

### Auto-push configurado

A cada `git commit`, o projeto é enviado automaticamente ao GitHub via hook `post-commit` (`.git/hooks/post-commit`).

```bash
git add .
git commit -m "mensagem do commit"
# o push acontece automaticamente após o commit
```

---

## Projetos Ativos

### 1. agencia-esteira (principal)
- **Localização:** `c:\Users\borge\OneDrive\Desktop\codigos py vs\agencia-esteira\`
- **Stack:** Next.js 14 (App Router) + TypeScript + Tailwind CSS + Supabase
- **Deploy:** https://agencia-esteira.vercel.app
- **Vercel token:** (ver .env local — não commitar)
- **Supabase:** projeto `fxxijiaisxmfhchgbiul`
- **Repo GitHub:** `github.com/borgesrodri4-bot/agencia-esteira`
- **Descrição:** Sistema interno de gestão de clientes da agência Kolhey — esteira de 7 fases com checklists, SLAs e progresso por fase

### 2. bot.py (Telegram)
- **Localização:** `c:\Users\borge\OneDrive\Desktop\codigos py vs\claudepy\bot.py`
- **Descrição:** Bot Telegram assistente pessoal com Claude AI

---

## Skills Instalados (`~/.claude/skills/`)

| Skill | Arquivo | Descrição |
|---|---|---|
| `kolhey-brand` | `kolhey-brand.md` | Manual de marca completo da Kolhey — paleta, tipografia, classes Tailwind, regras de design. Usar SEMPRE no projeto agencia-esteira |
| `agente-designer` | `agente-designer.md` | Agente elite de UI/UX e frontend. Declara direção estética antes de codar, produz código production-ready com todos os estados |

**Combinação recomendada para agencia-esteira:** `kolhey-brand` + `agente-designer`

---

## Projeto agencia-esteira — Contexto Completo

### Marca Kolhey
- **Cores:** navy `#0f2f48` (fundo), `#1a3d54` (sidebar), `#235475` (cards), laranja `#f28933` (destaque/CTA), terra `#c79982`
- **Fontes:** Cinzel (display/logo) + Montserrat (corpo)
- **Logo:** K**O**LHEY — o "O" é sempre laranja
- **Mascote:** Onça-pintada tribal laranja — usada como watermark (4% opacidade) na zona de trabalho, grande no login, pequena na sidebar
- **Slogan:** "Resultados que se cultivam" (Montserrat italic light)

### Arquivos de Imagem (public/)
- `onca-transparent.png` — onça tribal laranja com fundo transparente (1024×1024, processada com Pillow)
- `onca-kolhey.jpg` — logo 3D original (fundo escuro)

### Estrutura de Rotas
```
/login              — autenticação (split-panel: form esquerda + onça direita)
/dashboard          — painel geral com saudação, stats e grade de clientes
/clientes           — listagem com busca e filtros
/clientes/novo      — formulário de cadastro
/clientes/[id]      — visão geral + checklists por fase
/clientes/[id]/[fase] — checklist interativo da fase
/esteira            — documento de referência estático das 7 fases
```

### Banco de Dados (Supabase)
Tabelas: `profiles`, `clients`, `checklist_items`, `checklist_responses`, `phase_history`

### As 7 Fases da Esteira
1. Captação · 2. Diagnóstico · 3. Onboarding · 4. Execução · 5. Otimização · 6. Relatório · 7. Retenção

### Deploy
```bash
npx vercel deploy --prod --token="$VERCEL_TOKEN" --yes --scope="borgesrodri4-bots-projects"
```

---

## Pasta `prompts/`

Referências rápidas de prompts e skills:

| Arquivo | Conteúdo |
|---|---|
| `kolhey_design_prompt.md` | Tokens CSS, direção criativa, tipografia, animações, estrutura de seções, checklist de qualidade Kolhey |
| `agente-designer.md` | Cópia do skill agente-designer |
| `agencia_marketing_esteira.md` | Conteúdo das 7 fases, SLAs e KPIs |
| `system_prompt_agencia.py` | System prompt da agência |

---

## Convenções do Projeto agencia-esteira

- **Nunca** usar preto puro como fundo — usar navy `#0f2f48`
- **Nunca** usar dourado/gold — usar laranja `#f28933`
- **Nunca** usar Inter/Roboto/Arial como fonte principal
- **Sempre** SVG inline para ícones, nunca emoji
- **Sempre** `font-display` (Cinzel) só para logo/números grandes
- **Sempre** `font-sans` (Montserrat) no corpo
- Animações: 150–300ms, `ease-out` para entradas
- Focus rings em laranja para acessibilidade
- Skeletons animados no lugar de "Carregando..."
- Mobile: bottom nav 56px, touch targets ≥ 44px
