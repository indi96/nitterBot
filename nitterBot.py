import telebot
import html

SEARCH_WORDS = ['twitter.com', 'x.com']
deleteModeForChatID = {}

bot = telebot.TeleBot('InsertTokenHere', parse_mode=None)


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message,
                 "Hello I am a telegram bot. I am here to convert https://twitter.com and https://twitter.com links to https://nitter.net/ links. Maintained by indi96"
                 "\n\n Use /toggleDeleteMode for enabling and disabling the delete mode")


@bot.message_handler(commands=['toggleDeleteMode'])
def send_welcome(message):
    global deleteModeForChatID
    chatID = message.chat.id
    registration_service(chatID)
    if deleteModeForChatID[chatID]:
        bot.reply_to(message, "Messages that contain twitter.com or x.com links are now displayed")
        deleteModeForChatID[chatID] = False
    else:
        bot.reply_to(message, "Messages that contain twitter.com or x.com links are now deleted. \n" +
                     "Please give the bot the necessary permissions!")
        deleteModeForChatID[chatID] = True


@bot.message_handler(func=lambda message: any(word in message.text for word in SEARCH_WORDS))
def respond_to_specific_words(message):
    edit_and_send(message)
    global deleteModeForChatID
    if deleteModeForChatID[message.chat.id]:
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)


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


def registration_service(chatID):
    global deleteModeForChatID
    if chatID not in deleteModeForChatID:
        deleteModeForChatID[chatID] = False


bot.infinity_polling()
