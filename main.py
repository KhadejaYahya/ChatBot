import os
from dotenv import load_dotenv
import telebot
import time
import random

load_dotenv()
my_secret = os.getenv("API_KEY")
x = ["الله يعين", "الله يعين ، مدري شقولك بس الله يعين", "الله ييسرها"]

random.seed(time.time())

bot = telebot.TeleBot(my_secret)


@bot.message_handler(content_types=['text'])
def haltma(message):
    bot.reply_to(message, random.choice(x))


bot.polling()
