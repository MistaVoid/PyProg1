import telebot

bot = telebot.TeleBot('6901574297:AAHLowQb2S8PScSRNtfxq5tFwN9f2vkmlpQ')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет!')

bot.polling(none_stop=True)
