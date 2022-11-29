import telebot
from flask import Flask, request
import os

app = Flask(__name__)
TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def message_start(message):
    bot.send_message(message.chat.id, "Nice to see you in Morty and Osip Bot. Type \"Help\" for some PyHelp")


@bot.message_handler(commands=['Help'])
def message_help(message):
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)

    with open('py_help.txt') as file:
        helper = [item.split(',') for item in file]

        for title, link in helper:
            link_button = telebot.types.InlineKeyboardButton(text=title.strip(), url=link.strip())
            keyboard.add(link_button)

        bot.send_message(message.chat.id, "Python Built-In-Types", reply_markup=keyboard)
