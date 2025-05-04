import random
from datetime import datetime
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

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

# Список мотиваційних фраз
motivations = [
    "Кожен день — це шанс зробити крок до своїх мрій.",
    "Не бійся програти. Бійся не спробувати.",
    "Ти здатен на більше, ніж думаєш.",
    "Все, що тобі потрібно для успіху — це віра в себе.",
    "Крок за кроком, ти досягнеш мети!"
]

# Функція для команди /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Привіт! Я твій помічник. Що зробимо сьогодні?')

# Функція для команди /motivation
async def motivation(update: Update, context: ContextTypes.DEFAULT_TYPE):
    selected_motivation = random.choice(motivations)
    await update.message.reply_text(f"Мотиваційна фраза: {selected_motivation}")

# Функція для команди /quote
async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    selected_quote = random.choice(quotes)
    await update.message.reply_text(f"Цитата на сьогодні: {selected_quote}")

# Функція для команди /challenge
async def challenge(update: Update, context: ContextTypes.DEFAULT_TYPE):
    selected_challenge = random.choice(challenges)
    await update.message.reply_text(f"Твій челендж на сьогодні:\n\n{selected_challenge}")

# Створюємо додаток і додаємо хендлери для кожної команди
app = ApplicationBuilder().token('7938270207:AAHUYWrqzNBv5DuoY6KsfJ7vDBF2GJ4dRjA').build()



from datetime import datetime
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Переклад назв днів
ua_days = {
    "Monday": "Понеділок", "Tuesday": "Вівторок", "Wednesday": "Середа",
    "Thursday": "Четвер", "Friday": "П’ятниця", "Saturday": "Субота", "Sunday": "Неділя"
}

# Функція для визначення графіка роботи
def get_work_schedule():
    today = datetime.now()
    date_limit = datetime(today.year, 4, 21)  # після 20 квітня — нічних змін нема
    dow = ua_days[today.strftime("%A")]
    if today < date_limit and dow in ["Середа", "Четвер", "П’ятниця", "Субота", "Неділя"]:
        return "Нічна зміна 20:00–08:00"
    else:
        return "Сьогодні вихідний або зміна ще не визначена"
# Функція для розкладу автобуса
def get_bus_time():
    return "🚍 Автобус:\n1-а зміна: 04:35\n2-а зміна: 16:38"

# Функція чергувань за датою
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

# Команди бота
async def work(update: Update, context: ContextTypes.DEFAULT_TYPE):
    day = ua_days[datetime.now().strftime("%A")]
    schedule = get_work_schedule()
    await update.message.reply_text(f"📅 Сьогодні: {day}\n🕒 {schedule}")

async def bus(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(get_bus_time())

async def shift(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(get_shift())
# Додаємо хендлери
app.add_handler(CommandHandler('start', start))
app.add_handler(CommandHandler('motivation', motivation))
app.add_handler(CommandHandler('quote', quote))
app.add_handler(CommandHandler('challenge', challenge))
app.add_handler(CommandHandler('work', work))
app.add_handler(CommandHandler('bus', bus))
app.add_handler(CommandHandler('shift', shift))
# Запускаємо бота
app.run_polling()


app.run_polling()
print("Бот запущено.")
app.run_polling()
print("Бот запущено.")
app.run_polling()




