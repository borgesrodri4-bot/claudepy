"""
Assistente Pessoal no Telegram com Claude AI
Uso: python bot.py
"""

import os
import logging
from dotenv import load_dotenv
import anthropic
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
ALLOWED_USER_ID = os.getenv("ALLOWED_USER_ID")  # opcional: restringe acesso

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

# Histórico de conversa por chat_id
conversation_history: dict[int, list[dict]] = {}

SYSTEM_PROMPT = """Você é um assistente pessoal inteligente e prestativo, integrado ao Telegram.
Você responde sempre em português brasileiro de forma clara, direta e amigável.
Você pode ajudar com: tarefas do dia a dia, perguntas gerais, redação de textos,
análise de informações, planejamento, programação, e muito mais.
Seja conciso quando possível, mas detalhado quando necessário."""


def is_allowed(user_id: int) -> bool:
    if not ALLOWED_USER_ID:
        return True
    return str(user_id) == ALLOWED_USER_ID


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    if not is_allowed(user_id):
        await update.message.reply_text("Acesso não autorizado.")
        return

    conversation_history[user_id] = []
    await update.message.reply_text(
        "Olá! Sou seu assistente pessoal com Claude AI. 🤖\n\n"
        "Pode me perguntar qualquer coisa!\n\n"
        "Comandos disponíveis:\n"
        "/start — reinicia a conversa\n"
        "/limpar — apaga o histórico\n"
        "/ajuda — mostra esta mensagem"
    )


async def limpar(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    if not is_allowed(user_id):
        return

    conversation_history[user_id] = []
    await update.message.reply_text("Histórico apagado. Começando do zero! 🗑️")


async def ajuda(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "🤖 *Assistente Pessoal — Claude AI*\n\n"
        "Basta me enviar uma mensagem e eu responderei!\n\n"
        "Comandos:\n"
        "/start — reinicia a conversa\n"
        "/limpar — apaga o histórico da conversa\n"
        "/ajuda — exibe este menu",
        parse_mode="Markdown",
    )


async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    if not is_allowed(user_id):
        await update.message.reply_text("Acesso não autorizado.")
        return

    texto = update.message.text
    if not texto:
        return

    if user_id not in conversation_history:
        conversation_history[user_id] = []

    conversation_history[user_id].append({"role": "user", "content": texto})

    # Indica que está digitando
    await context.bot.send_chat_action(
        chat_id=update.effective_chat.id, action="typing"
    )

    try:
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=2048,
            system=SYSTEM_PROMPT,
            messages=conversation_history[user_id],
        )

        resposta = response.content[0].text
        conversation_history[user_id].append(
            {"role": "assistant", "content": resposta}
        )

        # Limita histórico a 20 mensagens para não estourar tokens
        if len(conversation_history[user_id]) > 20:
            conversation_history[user_id] = conversation_history[user_id][-20:]

        await update.message.reply_text(resposta)

    except anthropic.APIError as e:
        logger.error("Erro na API do Claude: %s", e)
        await update.message.reply_text(
            "Erro ao conectar com o Claude. Tente novamente em instantes."
        )
    except Exception as e:
        logger.error("Erro inesperado: %s", e)
        await update.message.reply_text("Ocorreu um erro inesperado. Tente novamente.")


def main() -> None:
    if not TELEGRAM_TOKEN:
        raise ValueError("TELEGRAM_TOKEN não definido no arquivo .env")
    if not ANTHROPIC_API_KEY:
        raise ValueError("ANTHROPIC_API_KEY não definido no arquivo .env")

    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("limpar", limpar))
    app.add_handler(CommandHandler("ajuda", ajuda))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))

    logger.info("Bot iniciado. Aguardando mensagens...")
    app.run_polling()


if __name__ == "__main__":
    main()
