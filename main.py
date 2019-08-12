import telebot 
import os

import random

from translate import translate
from api import get_cat

token = '705947275:AAEWgtl8pIItm95eYAcszsopaW3_dxmRHGE'

bot = telebot.TeleBot(token)

upd = bot.get_updates()




@bot.message_handler(commands=['start'])        
def handle_start(message):
  start_markup = telebot.types.ReplyKeyboardMarkup(True, False) #èçìåíåèå ðàçìåðà êëàâû
  start_markup.row('/start', '/help','/stop')
  start_markup.row('cлучайное фото', 'образование')
  start_markup.row('милый котик')
  bot.send_message(message.from_user.id, 'Добро пожаловать...', reply_markup=start_markup)
    
@bot.message_handler(commands=['help'])
def handle_help(message):

  help_markup = telebot.types.ReplyKeyboardMarkup(True, False)
  bot.send_message(message.from_user.id, 'Так же доступна дополнительная команда с rus => eng: /translate ',reply_markup = help_markup)


@bot.message_handler(commands=['stop'])
def handle_stop(message):

  stop_markup = telebot.types.ReplyKeyboardRemove()
  bot.send_message(message.from_user.id, 'Клавиатура спрятана, чтобы ее включить напишите команду : /start', reply_markup=stop_markup)


@bot.message_handler(content_types=['text'])
def handle_text(message,):
  chat_id = message.json['chat']['id']
  text = message.text

  if text == 'cлучайное фото':
    directory = './images/'
    all_files_in_directory = os.listdir(directory)
    random_file = random.choice(all_files_in_directory)
    img = open(directory + random_file, 'rb')
    bot.send_photo(chat_id, img)
    img.close()
  elif text == 'образование':
    directory = './document/'
    all_files_in_directory = os.listdir(directory)
    random_file = random.choice(all_files_in_directory)
    document = open(directory + random_file, 'rb')
    bot.send_document(chat_id, document)
    document.close()
  elif text == 'милый котик':
    img = get_cat() 
    markup = telebot.types.InlineKeyboardMarkup()
    button_site= telebot.types.InlineKeyboardButton(text='Котики тут', url='https://thecatapi.com/')
    markup.add(button_site)
    bot.send_photo(chat_id, img)
    bot.send_message(chat_id, "API с котиками", reply_markup = markup)
    pass
  elif text[:10:1] == '/translate':
    bot.send_message(chat_id, translate(text[11::1]))
    pass
    
  else:
    error_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    error_markup.row('/start')
    bot.send_message(message.from_user.id, 'Я вас не понимаю, попробуйте нажать на кнопку', reply_markup=error_markup)
    
        
                

bot.polling(none_stop=True, interval= 1)