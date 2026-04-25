import telebot
from flask import Flask, request

TOKEN = '8270894240:AAEv2LJRnE2jzesthGiKYLeLvi6MwRK366k'
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# Ganti 'kazuekurosaki' dengan username GitHub Anda jika berbeda
WEB_APP_URL = "https://kazuekurosaki.github.io/zentrix-ai-hub/"

@app.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

@app.route("/")
def webhook():
    bot.remove_webhook()
    # Ganti 'usernameanda' dengan username PythonAnywhere Anda nanti
    bot.set_webhook(url='https://kazuekurosaki.pythonanywhere.com/' + TOKEN)
    return "Webhook Set!", 200

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.InlineKeyboardMarkup()
    btn = telebot.types.InlineKeyboardButton(text="🚀 Open Zentrix Dashboard", url=WEB_APP_URL)
    markup.add(btn)
    
    bot.send_message(
        message.chat.id, 
        "Welcome to *Zentrix AI Hub*.\n\nPremium AI Assistant for Global Users.", 
        parse_mode='Markdown', 
        reply_markup=markup
    )

if __name__ == "__main__":
    app.run()
