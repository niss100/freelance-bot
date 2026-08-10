import os
import telebot
from telebot import types

# Render Environment Variables-dən oxuyur
TOKEN = os.environ.get("TOKEN")
MY_CHAT_ID = os.environ.get("MY_CHAT_ID")

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def welcome_complete_system(message):
    markup = types.InlineKeyboardMarkup(row_width=1)

    btn1 = types.InlineKeyboardButton(
        text="🤖 Order: Telegram Bot Development", callback_data="order_bot"
    )
    btn2 = types.InlineKeyboardButton(
        text="📊 Order: Web Scraping (Data to Excel)",
        callback_data="order_scraping",
    )
    btn3 = types.InlineKeyboardButton(
        text="⚙️ Order: Automation Scripts", callback_data="order_automation"
    )
    btn4 = types.InlineKeyboardButton(
        text="📈 Order: Data Cleaning & Analysis",
        callback_data="order_analysis",
    )
    btn5 = types.InlineKeyboardButton(
        text="🧠 Order: AI & ChatGPT Integration", callback_data="order_ai"
    )
    btn_question = types.InlineKeyboardButton(
        text="❓ Ask a Question / Задать вопрос",
        url="https://t.me/your_telegram_username",
    )

    markup.add(btn1, btn2, btn3, btn4, btn5, btn_question)

    bot.reply_to(
        message,
        """Hello! Welcome to Nigar's official freelance bot. 🚀
Здравствуйте! Добро пожаловать в официальный бот Нигяр.

💼 My Python Services / Мои Услуги:
1️⃣ Telegram Bot Development / Разработка ботов
2️⃣ Web Scraping (Data To Excel) / Парсинг данных
3️⃣ Automation Scripts / Скрипты автоматизации
4️⃣ Data Cleaning & Analysis / Очистка и анализ данных
5️⃣ AI & ChatGPT Integration / Интеграция ИИ и ИИ-ботов

👇 Select a service to order or ask a question:
👇 Выберите услугу для заказа или задайте вопрос:""",
        reply_markup=markup,
    )


@bot.callback_query_handler(func=lambda call: call.data.startswith("order_"))
def handle_order(call):
    username = (
        call.from_user.username
        if call.from_user.username
        else "No Username"
    )
    first_name = call.from_user.first_name

    service_name = ""
    if call.data == "order_bot":
        service_name = "Telegram Bot Development"
    elif call.data == "order_scraping":
        service_name = "Web Scraping"
    elif call.data == "order_automation":
        service_name = "Automation Scripts"
    elif call.data == "order_analysis":
        service_name = "Data Cleaning & Analysis"
    elif call.data == "order_ai":
        service_name = "AI & ChatGPT Integration"

    notification = (
        f"🚨 NEW FREELANCE ORDER!\n\n"
        f"👤 Client: {first_name} (@{username})\n"
        f"💼 Chosen Service: {service_name}"
    )

    bot.send_message(MY_CHAT_ID, notification)
    bot.answer_callback_query(call.id, "Order received! / Заказ принят!")
    bot.send_message(
        call.message.chat.id,
        "✅ Your order has been sent to Nigar. She will contact you soon!\n"
        "✅ Ваш заказ отправлен Нигяр. Она скоро свяжется с вами!",
    )


print("The ultimate 6-button freelance bot is running flawlessly...")
bot.infinity_polling()
