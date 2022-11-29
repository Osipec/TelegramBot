import telebot
from flask import Flask, request
import os

app = Flask(__name__)
TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def message_start(message):
    bot.send_message(message.chat.id, "Nice to see you in Morty and Osip Bot. Type String to see Python string methods")

@bot.message_handler(commands=['String'])
def message_string(message):
    pass
