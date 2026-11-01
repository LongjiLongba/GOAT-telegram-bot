import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = '9237071248:AAHaWLCD6oot7yAhoME6yxErngghiM7C71k'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        "🐐🐐GOAT SERVICE DIRECTORY 🤩🐐\n\n"
        "✅Official Channels & Chats: ✅\n\n"
        "Tap any button below to get started!"
    )
    
    markup = InlineKeyboardMarkup()
    
    btn_premium = InlineKeyboardButton(text="⭐ PREMIUM SERVICE", url="https://t.me/GOAT_SERVlCE1")
    btn_admin = InlineKeyboardButton(text="👨‍💼 Admin", url="https://t.me/GOAT_SERVlCE1")
    btn_shop = InlineKeyboardButton(text="🛍️ Online Shop", url="https://shoppy.gg/@GOATESHOPSERVICE")
    btn_channel = InlineKeyboardButton(text="📚 New Channel", url="https://t.me/GOATSERVICECHANEL")
    btn_group = InlineKeyboardButton(text="💬 Group Chat", url="https://t.me/GOATGROUPLINK")
    btn_support = InlineKeyboardButton(text="👨‍💻 Support", url="https://t.me/money_bitxh")
    
    markup.add(btn_premium)
    markup.add(btn_admin, btn_shop)
    markup.add(btn_channel, btn_group)
    markup.add(btn_support)

    bot.reply_to(message, welcome_text, reply_markup=markup)

print("Bot with buttons is running...")
bot.infinity_polling()

