import telebot
import html

SEARCH_WORDS = ['twitter.com', 'x.com']

bot = telebot.TeleBot('6612671822:AAGXHA2ITQpEBXH2lfRCpuwnE26VGAz4qL4', parse_mode=None)


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
    edit_and_send(message)


@bot.edited_message_handler(func=lambda message: any(word in message.text for word in SEARCH_WORDS))
def respond_to_edited_message(message):
    edit_and_send(message)


def edit_and_send(message):
    response = message.text
    for word in SEARCH_WORDS:
        response = response.replace(word, 'nitter.net')
    bot.send_message(message.chat.id,
                     '<b>Better with Nitter:</b>\n' + html.escape(response),
                     disable_web_page_preview=False,
                     parse_mode='HTML')


bot.infinity_polling()
