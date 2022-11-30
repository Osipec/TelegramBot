import telebot
from flask import Flask, request
import os
import wikipedia, re

app = Flask(__name__)
#TOKEN = os.environ.get("5843370296:AAHCrvwgiV6lKkpSiMzWMwNIs23Hd3z872I")
TOKEN = "5843370296:AAHCrvwgiV6lKkpSiMzWMwNIs23Hd3z872I"
bot = telebot.TeleBot(TOKEN)

#
# @bot.message_handler(commands=['start'])
# def message_start(message):
#     bot.send_message(message.chat.id, "Nice to see you in Morty and Osip Bot. Type \"Help\" for some PyHelp")
#
#
# @bot.message_handler(commands=['Help'])
# def message_help(message):
#     keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
#
#     with open('py_help.txt') as file:
#         helper = [item.split(',') for item in file]
#
#         for title, link in helper:
#             link_button = telebot.types.InlineKeyboardButton(text=title.strip(), url=link.strip())
#             keyboard.add(link_button)
#
#         bot.send_message(message.chat.id, "Python Built-In-Types", reply_markup=keyboard)
# bot.infinity_polling()
# Устанавливаем русский язык в Wikipedia
wikipedia.set_lang("ru")
# Чистим текст статьи в Wikipedia и ограничиваем его тысячей символов
def getwiki(s):
    try:
        ny = wikipedia.page(s)
        # Получаем первую тысячу символов
        wikitext = ny.content[:1000]
        # Разделяем по точкам
        wikimas = wikitext.split('.')
        # Отбрасываем всЕ после последней точки
        wikimas = wikimas[:-1]
        # Создаем пустую переменную для текста
        wikitext2 = ''
        # Проходимся по строкам, где нет знаков «равно» (то есть все, кроме заголовков)
        for x in wikimas:
            if not('==' in x):
                    # Если в строке осталось больше трех символов, добавляем ее к нашей переменной и возвращаем утерянные при разделении строк точки на место
                if(len((x.strip())) > 3):
                   wikitext2 = wikitext2 + x + '.'
            else:
                break
        # Теперь при помощи регулярных выражений убираем разметку
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\{[^\{\}]*\}', '', wikitext2)
        # Возвращаем текстовую строку
        return wikitext2
    # Обрабатываем исключение, которое мог вернуть модуль wikipedia при запросе
    except Exception as e:
        return 'В энциклопедии нет информации об этом'
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Отправьте мне любое слово, и я найду его значение на Wikipedia')
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, getwiki(message.text))
# Запускаем бота
bot.polling(none_stop=True, interval=0)