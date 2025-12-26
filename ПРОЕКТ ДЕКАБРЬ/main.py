from telebot import TeleBot
from bs4 import BeautifulSoup
from config import TOKEN


bot = TeleBot(TOKEN)





bot.infinity_polling()