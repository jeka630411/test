import telebot

bot = telebot.TeleBot("6911160758:AAERrTi8JMbDril1MiADOYnJrqC3RhLxIoI")


@bot.message_handler(commands=['start'])
def main(massage):
    bot.send_message(massage.chat.id, "привет")


    ееее