import telebot
import schedule
from threading import Thread
from telebot import types
from datetime import date
from time import sleep
from goal_check import *


API_KEY = ''
bot = telebot.TeleBot(API_KEY)
users = set()

markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
markup.add('SOCCER⚽️', 'BASKETBALL🏀')

soccer_info = soccer()
basketball_info = basketball()


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hi, I'm SportStatsBot. I will send You info about soccer and basketball upcoming events")
    users.add(message.chat.id)
    today = date.today().strftime("%d/%m/%Y").replace('/','.')
    text = f'Today is {today}, Would You like to get some stats info on:'
    msg = bot.reply_to(message, text, reply_markup=markup)
    bot.register_next_step_handler(msg, process_step)


def process_step(message):
    if message.text=='SOCCER⚽️':
        bot.send_message(message.chat.id, soccer_info)
        bot.send_message(message.chat.id, 'If You want to get updated info (info updates twice a day) -> send /getinfo')
    elif message.text=='BASKETBALL🏀':
        bot.send_message(message.chat.id, basketball_info)


@bot.message_handler(commands=['getinfo'])
def add_mail(message):
    today = date.today().strftime("%d/%m/%Y").replace('/','.')
    text = f'Today is {today}, Would You like to get some stats info on:'
    msg = bot.reply_to(message, text, reply_markup=markup)
    bot.register_next_step_handler(msg, process_step)


def schedule_checker():
    while True:
        schedule.run_pending()
        sleep(1)


def function_to_run():
    global soccer_info, basketball_info
    soccer_info = soccer()
    basketball_info = basketball()


if __name__ == "__main__":
    schedule.every().day.at("11:59").do(function_to_run)
    schedule.every().day.at("23:59").do(function_to_run)
    Thread(target=schedule_checker).start() 
    bot.polling()
