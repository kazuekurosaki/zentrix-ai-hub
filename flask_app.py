import telebot
from flask import Flask, request

TOKEN = '8270894240:AAEv2LJRnE2jzesthGiKYLeLvi6MwRK366k' # Token Anda
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

URL_WEBHOOK = 'https://kazuekurosaki.pythonanywhere.com/'

@app.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

@app.route("/")
def webhook():
    bot.remove_webhook()
    status = bot.set_webhook(url=URL_WEBHOOK + TOKEN)
    if status:
        return "Zentrix Bot is Active!", 200
    else:
        return "Webhook Setup Failed!", 500

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.InlineKeyboardMarkup()
    url_web = "https://kazuekurosaki.github.io/zentrix-ai-hub/"
    btn = telebot.types.InlineKeyboardButton(text="🚀 Open Dashboard", url=url_web)
    markup.add(btn)
    bot.send_message(message.chat.id, "Welcome to *Zentrix AI Premium*.\nClick below to start.", parse_mode='Markdown', reply_markup=markup)
