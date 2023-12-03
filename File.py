import webbrowser
from telebot import types
import telebot

bot = telebot.TeleBot("6911160758:AAERrTi8JMbDril1MiADOYnJrqC3RhLxIoI")

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    bt1 = types.KeyboardButton("Перейти на сайт")
    markup.row(bt1)
    bt2 = types.KeyboardButton("Удалить фото")
    bt3 = types.KeyboardButton("Изменить текст")
    markup.row(bt2, bt3)
    #file = open("./Photo.mp4", "rb")
    # bot.send_video(message.chat.id, file, reply_markup=markup)
    # file = open("./Photo.mp3", "rb")
    # bot.send_audio(message.chat.id, file, reply_markup=markup)
    #file = open("./Photo.png", "rb")
    #bot.send_photo(message.chat.id, file, reply_markup=markup)
    #bot.send_message(message.chat.id, "Привет", reply_markup=markup)
    bot.register_next_step_handler(message, on_klic)

def on_klic(message):
    if message.text == "Перейти на сайт":
        bot.send_message(message.chat.id, "Website is open ")
    elif message.text == "Перейти на сайт":
        bot.send_message(message.chat.id, "Удалить фото")


@bot.message_handler(content_types=["photo"])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    bt1 = types.InlineKeyboardButton("Перейти на сайт", url="https://www.google.com.ua/?hl=ru")
    markup.row(bt1)
    bt2 = types.InlineKeyboardButton("Удалить фото", callback_data="delete")
    bt3 = types.InlineKeyboardButton("Изменить текст",callback_data="edit")
    markup.row(bt2, bt3)
    bot.send_message(message, "Какое красивое фото!", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == "delete":
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == "edit":
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)


@bot.message_handler(commands=["site", "website"])
def site(message):
    webbrowser.open("https://itproger.com")


@bot.message_handler(commands=['start', "main", "hello"])
def main(massage):
    bot.send_message(massage.chat.id, f"привет, {massage.from_user.first_name} {massage.from_user.last_name}")

@bot.message_handler(commands=["help"])
def main(massage):
    bot.send_message(massage.chat.id, "<b> Help </b> <em> <u>information </u> </em> ", parse_mode="html")


@bot.message_handler(commands=["info"])
def main(massage):
    bot.send_message(massage.chat.id, (massage))


@bot.message_handler()
def info(message):
    if message.text.lower() == "привет":
        bot.send_message(message.chat.id, f"привет, {message.from_user.first_name} {message.from_user.last_name}")
    elif message.text.lower() == "id":
        bot.reply_to(message, f'ID: {message.from_user.id}')

bot.polling(none_stop=True)sage(massage.chat.id, "привет")