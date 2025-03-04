import telebot
from bot_logic import gen_pass
from bot_game import game

# Замени 'TOKEN' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("7287636434:AAFiKGvrN7wcyeAPRw2tmYS44T5jU0usmHM")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['game'])
def send_game(message):
    bot.reply_to(message, game(1))

@bot.message_handler(commands=['password'])
def send_password(message):
    bot.reply_to(message, gen_pass(10))

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()