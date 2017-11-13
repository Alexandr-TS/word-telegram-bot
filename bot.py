# -*- coding: utf-8 -*-
import config
import telebot
import random
from telebot import types

words = []

#f = open('words.txt', 'r')
#for i in range(0, 1002):
    #words.append(f.readline().rstrip())
#f.close()

#f2 = open('words.txt', 'w')
#s = ""
#for i in range(0, 1002):
    #s = s + words[i] + " "
#f2.write(s)

bot = telebot.TeleBot(config.token)

words_file = open('words.txt', 'r')
words = words_file.readline().split()
print(len(words))

@bot.message_handler(commands=['start'])
def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(word_but) for word_but in ['Одно слово', 'Много слов']])
    msg = bot.send_message(m.chat.id, 'Привет', reply_markup=keyboard)   
    bot.register_next_step_handler(msg, word_but)

@bot.message_handler(func=lambda message: message.text == u'Одно слово')
def word_but(m):
    if (m.text == 'Одно слово'):
        number = random.randint(0, len(words))
        bot.send_message(m.chat.id, words[number])
        
@bot.message_handler(func=lambda message: message.text == u'Много слов')
def many_word_but(m):
    if (m.text == 'Много слов'):
        for i in range(10):
            number = random.randint(0, len(words))
            bot.send_message(m.chat.id, words[number])
    

#@bot.message_handler(content_types=["text"])
#def repeat_all_messages(message):
    #bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.polling()