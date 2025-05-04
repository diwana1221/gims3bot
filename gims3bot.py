import os
import random
from datetime import datetime
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Мотиваційні цитати
quotes = [
    "Сьогодні — ідеальний день почати щось нове.",
    "Навіть маленький крок — це прогрес.",
    "Успіх приходить до тих, хто не здається.",
    "Твоя енергія — твоя суперсила!",
    "Ти можеш більше, ніж думаєш."
]

# Челенджі
challenges = [
    "💧 Випий 2 л води сьогодні.",
    "🚶 Пройди 8000 кроків.",
    "📵 Вимкни телефон на 1 годину.",
    "📚 Почитай 10 сторінок книги.",
    "🧘‍♀️ Зроби 5 хвилин медитації або дихання."
]

# Українські дні тижня
ua_days = {
    "Monday": "Понеділок", "Tuesday": "Вівторок", "Wednesday": "Середа",
    "Thursday": "Четвер", "Friday": "П’ятниця", "Saturday": "Субота", "Sunday": "Неділя"
}

# Робочий графік
def get_work_schedule():
    today = datetime.now()
    date_limit = datetime(today.year, 4, 21)
    dow = ua_days[today.strftime("%A")]
    if today < date_limit and dow in ["Середа", "Четвер", "П’ятниця", "Субота", "Неділя"]:
        return "Нічна зміна 20:00–08:00"
    else:
        return "Сьогодні вихідний або зміна ще не визначена"

# Автобус
def get_bus_time():
    return "🚍 Автобус:\n1-а зміна: 04:35\n2-а зміна: 16:38"

# Чергування
def get_shift():
    today = datetime.now().date()
    if datetime(2025, 4, 28).date() <= today <= datetime(2025, 5, 4).date():
        return "👩‍⚕️ Сьогодні чергує: Оксана"
    elif datetime(2025, 5, 5).date() <= today <= datetime(2025, 5, 12).date():
        return "👩‍⚕️ Сьогодні чергує: Марія"
    elif datetime(2025, 5, 13).date() <= today <= datetime(2025, 5, 20).date():
        return "👩‍⚕️ Сьогодні чергує: Діана"
    else:
        return "Чергувань на цю дату не заплановано"

# Меню кнопок
main_menu = ReplyKeyboardMarkup(
    [
        ["🕒 Робота", "🚍 Автобус"],
        ["👩‍⚕️ Чергування", "💬 Цитата"],
        ["💪 Челендж"]
    ],
    resize_keyboard=True
)

# Команда /start — меню
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привіт! Обери опцію з меню 👇",
        reply_markup=main_menu
    )

# Обробка кнопок
# Обробка кнопок з постійним меню
# Обробка кнопок
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "🕒 Робота":
        day = ua_days[datetime.now().strftime("%A")]
        await update.message.reply_text(f"📅 Сьогодні: {day}\n🕒 {get_work_schedule()}")
    elif text == "🚍 Автобус":
        await update.message.reply_text(get_bus_time())
    elif text == "👩‍⚕️ Чергування":
        await update.message.reply_text(get_shift())
    elif text == "💬 Цитата":
        await update.message.reply_text(random.choice(quotes))
    elif text == "💪 Челендж":
        await update.message.reply_text(random.choice(challenges))
    else:
        await update.message.reply_text("Я не зрозумів 🧐 Обери щось із меню.")


    await update.message.reply_text(response, reply_markup=main_menu)

# Запуск бота
app = ApplicationBuilder().token(os.environ['7938270207:AAHUYWrqzNBv5DuoY6KsfJ7vDBF2GJ4dRjA']).build()
app.add_handler(CommandHandler('start', start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()
