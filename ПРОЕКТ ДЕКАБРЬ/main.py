from telebot import TeleBot
from bs4 import BeautifulSoup
from config import TOKEN
from parser_copy import screach
import string

bot = TeleBot(TOKEN)

@bot.message_handler(commands=["info"])
def info(message):
    bot.reply_to(message, "Напишите название болезни")
    bot.register_next_step_handler(message, pars)
def pars(message):
    all_text = screach(message.text)
    if all_text == "":
        bot.reply_to(message, "Призошла непривидинная ошибка")
    else:
        all_text = " ".join(all_text)
        for i in range(1,20):
            all_text = all_text.replace(f"[{i}]", "")
        bot.reply_to(message, all_text)



bot.polling()