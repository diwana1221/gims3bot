import os
import random
from datetime import datetime
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters


# Список челенджів
challenges = [
    "Пройди 8000 кроків сьогодні!",
    "Не користуйся соцмережами 2 години.",
    "Зроби 10 хвилин фізичних вправ.",
    "Прочитай 5 сторінок книги.",
    "Подзвони близькій людині.",
    "Випий 2 літри води.",
    "Вивчи 5 нових англійських слів.",
    "Напиши план на завтра.",
    "Поприбирай на робочому столі.",
    "Відпочинь без телефона 30 хвилин."
]

# Мотиваційні цитати
quotes = [
    "Ти зможеш, якщо будеш старатися!",
    "Не бігай за успіхом. Стань успіхом!",
    "Труднощі — це сходи до успіху.",
    "Ніколи не здавайся!",
    "Великий успіх починається з маленьких кроків."
]

# Створення головного меню
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        ["Мій графік", "Автобус"],
        ["Чергування", "Челендж"],
        ["Цитата"]
    ],
    resize_keyboard=True
)

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привіт! Обери дію з меню нижче ⬇️",
        reply_markup=main_menu
    )

# /challenge
async def challenge(update: Update, context: ContextTypes.DEFAULT_TYPE):
    selected = random.choice(challenges)
    await update.message.reply_text(f"Твій челендж на сьогодні:\n\n{selected}")

# /quote
async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    selected = random.choice(quotes)
    await update.message.reply_text(f"Цитата на сьогодні:\n\n{selected}")

# Графік роботи
async def schedule(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Твій графік: нічні зміни середа–неділя до 20 квітня.")

# Автобус
async def bus(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Автобус:\n• Перша зміна: 04:35\n• Друга зміна: 16:38")

# Чергування
async def duty(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Чергування:\n"
        "• Оксана: 28 квітня – 4 травня\n"
        "• Марія: 5 – 12 травня\n"
        "• Діана: 13 – 20 травня"
    )

# Обробка кнопок меню
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "Челендж":
        await challenge(update, context)
    elif text == "Цитата":
        await quote(update, context)
    elif text == "Мій графік":
        await schedule(update, context)
    elif text == "Автобус":
        await bus(update, context)
    elif text == "Чергування":
        await duty(update, context)
    else:
        await update.message.reply_text("Не розумію. Обери команду з меню.")

# Запуск
app = ApplicationBuilder().token("7938270207:AAHUYWrqzNBv5DuoY6KsfJ7vDBF2GJ4dRjA").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()


app = ApplicationBuilder().token('7938270207:AAHUYWrqzNBv5DuoY6KsfJ7vDBF2GJ4dRjA').build()
app.run_polling()  # This will handle updates by polling the server.