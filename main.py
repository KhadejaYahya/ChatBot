import os
import telebot
import time
import random


# my_secret = os.environ['API_KEY']
x = ["الله يعين", "الله يعين ، مدري شقولك بس الله يعين", "الله ييسرها"]

random.seed(time.time())

bot = telebot.TeleBot('5527949956:AAFSoW3lXflQ1WzFtjymt2QqgLOwoMUy340')


@bot.message_handler(content_types=['text'])
def haltma(message):
    bot.reply_to(message, random.choice(x))


bot.polling()