# import webbrowser
# from telebot import types
# import telebot
#
# bot = telebot.TeleBot("6911160758:AAERrTi8JMbDril1MiADOYnJrqC3RhLxIoI")
#
# @bot.message_handler(commands=["start"])
# def start(message):
#     markup = types.ReplyKeyboardMarkup()
#     bt1 = types.KeyboardButton("Перейти на сайт")
#     markup.row(bt1)
#     bt2 = types.KeyboardButton("Удалить фото")
#     bt3 = types.KeyboardButton("Изменить текст")
#     markup.row(bt2, bt3)
#     #file = open("./Photo.mp4", "rb")
#     # bot.send_video(message.chat.id, file, reply_markup=markup)
#     # file = open("./Photo.mp3", "rb")
#     # bot.send_audio(message.chat.id, file, reply_markup=markup)
#     #file = open("./Photo.png", "rb")
#     #bot.send_photo(message.chat.id, file, reply_markup=markup)
#     #bot.send_message(message.chat.id, "Привет", reply_markup=markup)
#     bot.register_next_step_handler(message, on_klic)
#
# def on_klic(message):
#     if message.text == "Перейти на сайт":
#         bot.send_message(message.chat.id, "Website is open ")
#     elif message.text == "Перейти на сайт":
#         bot.send_message(message.chat.id, "Удалить фото")
#
#
# @bot.message_handler(content_types=["photo"])
# def get_photo(message):
#     markup = types.InlineKeyboardMarkup()
#     bt1 = types.InlineKeyboardButton("Перейти на сайт", url="https://www.google.com.ua/?hl=ru")
#     markup.row(bt1)
#     bt2 = types.InlineKeyboardButton("Удалить фото", callback_data="delete")
#     bt3 = types.InlineKeyboardButton("Изменить текст",callback_data="edit")
#     markup.row(bt2, bt3)
#     bot.send_message(message, "Какое красивое фото!", reply_markup=markup)
#
#
# @bot.callback_query_handler(func=lambda callback: True)
# def callback_message(callback):
#     if callback.data == "delete":
#         bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
#     elif callback.data == "edit":
#         bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)
#
#
# @bot.message_handler(commands=["site", "website"])
# def site(message):
#     webbrowser.open("https://itproger.com")
#
#
# @bot.message_handler(commands=['start', "main", "hello"])
# def main(massage):
#     bot.send_message(massage.chat.id, f"привет, {massage.from_user.first_name} {massage.from_user.last_name}")
#
# @bot.message_handler(commands=["help"])
# def main(massage):
#     bot.send_message(massage.chat.id, "<b> Help </b> <em> <u>information </u> </em> ", parse_mode="html")
#
#
# @bot.message_handler(commands=["info"])
# def main(massage):
#     bot.send_message(massage.chat.id, (massage))
#
#
# @bot.message_handler()
# def info(message):
#     if message.text.lower() == "привет":
#         bot.send_message(message.chat.id, f"привет, {message.from_user.first_name} {message.from_user.last_name}")
#     elif message.text.lower() == "id":
#         bot.reply_to(message, f'ID: {message.from_user.id}')
#
# bot.polling(none_stop=True)sage(massage.chat.id, "привет")





# import telebot
# import requests
# import json
#
# bot = telebot.TeleBot("6911160758:AAERrTi8JMbDril1MiADOYnJrqC3RhLxIoI")
# API = "e86668551f34b2114923697539425293"
#
# previous_cities = []
#
#
# @bot.message_handler(commands=["start"])
# def start(message):
#     bot.send_message(message.chat.id, "Привет! Я бот погоды.")
#
#
# @bot.message_handler(commands=["start2"])
# def start2(message):
#     if previous_cities:
#         reply_message = "Предыдущие города и их температура:\n"
#         for city in previous_cities:
#             reply_message += f"{city.capitalize()}: {get_temperature(city)}°C\n"
#         bot.send_message(message.chat.id, reply_message)
#     else:
#         bot.send_message(message.chat.id, "Пока нет предыдущих городов.")
#
#
# @bot.message_handler(content_types=["text"])
# def get_weather(message):
#     city = message.text.strip().lower()
#
#     temperature = get_temperature(city)
#
#     if temperature is not None:
#         previous_cities.append(city)
#         bot.reply_to(message, f'Сейчас температура в городе {city.capitalize()}: {temperature}°C')
#     else:
#         bot.reply_to(message,
#                      f'Извините, не удалось получить информацию о погоде для {city}. Пожалуйста, попробуйте еще раз.')
#
#
# def get_temperature(city):
#     res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric")
#
#     if res.status_code == 200:
#         data = res.json()
#         temperature = data["main"]["temp"]
#         return temperature
#     else:
#         return None
#
#
# bot.polling(none_stop=True)


import telebot
import requests
import json

bot = telebot.TeleBot("6911160758:AAERrTi8JMbDril1MiADOYnJrqC3RhLxIoI")
API = "e86668551f34b2114923697539425293"

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я бот погоды.Напиши название города")

@bot.message_handler(content_types=["text"])
def get_weather(message):
    city = message.text.strip().lower()
    bot.send_message(message.chat.id, f"Ты написал мне город: {city}. ")
    res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric")
    if res.status_code == 200:

        data = json.loads(res.text)
        temp = data["main"]["temp"]
        bot.reply_to(message, f'Сейчас погода: {temp}')

        image = "sunny.jpg" if temp > 5.0 else "sunny-t.jpg"
        file = open("./" + image, "rb")
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, f'Город указан не верно')





bot.polling(none_stop=True)