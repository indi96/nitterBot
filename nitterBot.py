import telebot

SEARCH_WORDS = ['twitter.com', 'x.com']

bot = telebot.TeleBot('InsertTokenHere', parse_mode=None)


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message,
                 "Hello I am a telegram bot. I am here to convert https://twitter.com and https://twitter.com links to https://nitter.net/ links. Maintained by indi96")


@bot.message_handler(commands=['hilfe'])
def send_welcome(message):
    bot.reply_to(message,
                 "Hallo ich bin ein Telegramm Bot. Ich bin hier um https://twitter.com und https://twitter.com links in https://nitter.net/ links umzuwandeln. Wird gewartet von indi96")


@bot.message_handler(func=lambda message: any(word in message.text for word in SEARCH_WORDS))
def respond_to_specific_words(message):
    response = message.text
    for word in SEARCH_WORDS:
        response = response.replace(word, 'nitter.net')
    bot.send_message(message.chat.id,
                     '*Better with Nitter:*\n' + response,
                     disable_web_page_preview=False,
                     parse_mode='markdown')


bot.infinity_polling()
