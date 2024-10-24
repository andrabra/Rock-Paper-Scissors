import random
import telebot
from telebot import types

bot = telebot.TeleBot("***REMOVED***")

game = ["Камень", "Ножницы", "Бумага"]


@bot.message_handler(commands=['start'])
def handler_start(message):
    keyboard = types.ReplyKeyboardMarkup(True)

    button1 = types.KeyboardButton("Камень")
    button2 = types.KeyboardButton("Ножницы")
    button3 = types.KeyboardButton("Бумага")

    keyboard.add(button1, button2, button3)

    bot.reply_to(message, "Вы ходите первыми:", reply_markup=keyboard)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    random_object = random.choice(game)

    result = "Ничья!"

    if message.text == random_object:
        bot.reply_to(message, result)
    elif ((random_object == "Камень" and message.text == "Бумага")
          or (random_object == "Бумага" and message.text == "Ножницы")
          or (random_object == "Ножницы" and message.text == "Камень")):
        result = random_object
        message_template = f"Бот выбрал {random_object}, вы выиграли!"
        bot.reply_to(message, message_template)
        bot.send_message(message.chat.id, "Поздравляю!")
    else:
        result = random_object
        message_template = f"Бот выбрал {result}, вы проиграли!"
        bot.reply_to(message, message_template)
        bot.send_message(message.chat.id, "Попробуйте еще раз!")


bot.polling(none_stop=True)

