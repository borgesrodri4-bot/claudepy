---
name: telegram-bot
description: Gerencia o bot Telegram assistente pessoal com Claude AI. Ajuda a iniciar, parar, configurar e depurar o bot.
---

Você está gerenciando o **bot Telegram assistente pessoal** localizado em:
`C:\Users\borge\OneDrive\Desktop\codigos py vs\claudepy\`

## Arquivos principais
- `bot.py` — código principal do bot
- `.env` — tokens secretos (TELEGRAM_TOKEN, ANTHROPIC_API_KEY, ALLOWED_USER_ID)
- `.env.example` — template de configuração
- `requirements.txt` — dependências Python

## Comandos úteis

### Instalar dependências
```bash
cd "C:/Users/borge/OneDrive/Desktop/codigos py vs/claudepy"
pip install -r requirements.txt
```

### Iniciar o bot
```bash
cd "C:/Users/borge/OneDrive/Desktop/codigos py vs/claudepy"
python bot.py
```

### Verificar se o .env está configurado
```bash
cat "C:/Users/borge/OneDrive/Desktop/codigos py vs/claudepy/.env"
```

## Tarefas comuns

Quando o usuário pedir para:
- **iniciar o bot** → verificar se .env existe, instalar deps se necessário, rodar `python bot.py`
- **adicionar funcionalidade** → editar `bot.py`, adicionar handler e função correspondente
- **depurar erro** → ler os logs no terminal e o arquivo `bot.py`
- **trocar o modelo** → alterar o valor de `model=` na chamada `client.messages.create()`
- **mudar o comportamento** → editar a variável `SYSTEM_PROMPT` em `bot.py`
- **configurar tokens** → editar o arquivo `.env` com os valores corretos

## Estrutura do bot

O bot mantém histórico de conversa por `chat_id` (máximo 20 mensagens) e usa o
modelo `claude-sonnet-4-6` por padrão. Responde em português brasileiro.

Comandos disponíveis no Telegram:
- `/start` — reinicia a conversa
- `/limpar` — apaga o histórico
- `/ajuda` — exibe menu de ajuda

Agora, execute a tarefa que o usuário solicitou relacionada ao bot Telegram.
Se o usuário não especificou uma tarefa, mostre um resumo do status atual do projeto
(quais arquivos existem, se o .env está configurado, etc.) e pergunte o que ele quer fazer.
