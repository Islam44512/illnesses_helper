from telebot import TeleBot
from bs4 import BeautifulSoup
from config import TOKEN
from parser_copy import screach

bot = TeleBot(TOKEN)

@bot.message_handler(commands=["info"])
def info(message):
    bot.reply_to(message, "Напишите название болезни")
    bot.register_next_step_handler(message, pars)
def pars(message):
    all_text = screach(message.text)
    bot.reply_to(message, all_text)



bot.infinity_polling()