#!/bin/python
import telebot

api 7414300092:AAFl3VHliu9eSnxO0ahYZQAS0vQkvSq8QU0
bot = telebot.TeleBot(api)

@bot.message_handler(commands=['start'])
def send_welcome(message):
 bot.reply_to(message,'Halo Nama Gw hacker')

@bot.message_handler(commands=['help'])
def send_welcome(message):
 bot.reply_to(message,' Halo! Gw Cuma Bot Biasa ')

@bot.message_handler(commands=['runs'])
def send_welcome(message):
 bot.reply_to(message,'LARI ADA SETAN')

@bot.message_handler(commands=['duar'])
def send_welcome(message):
 bot.reply_to(message,'dwar mmk')
 
@bot.message_handler(commands=['tes'])
def send_welcome(message):
 bot.reply_to(message,'anjas lemot')

@bot.message_handler(commands=['halo'])
def send_welcome(message):
 bot.reply_to(message,'yg sopan tolol')
 
@bot.message_handler(commands=['pe'])
def send_welcome(message):
 bot.reply_to(message,'ya {}')
 
 
@bot.message_handler(commands=['list'])
def send_welcome(message):
 bot.reply_to(message,'/runs /duar /tes /afk /pe /halo /support')
 
@bot.message_handler(commands=['afk'])
def send_welcome(message):
 bot.reply_to(message,'babay ngab')

@bot.message_handler(commands=['support'])
def send_welcome(message):
 bot.reply_to(message,'kalo mau tanya ke @vohaunion aja ngab')


@bot.message_handler(func=lambda message: True)
def handle_all_message(message):
    if message.chat.type == "private":
        bot.reply_to(message, message.text)
    elif message.chat.type == "private":
        if('@username_of_your_bot' in message.text):
            bot.reply_to(message, "Hello to all!")

@bot.message_handler(func=lambda message: True)
def handle_all_message(message):
    if message.chat.type == "private":
        bot.reply_to(message, message.text)
    elif message.chat.type == "private":
        bot.reply_to(message, "Hello to all!")

print('bot mulai nih gan kalo gagal chat @xlaaf')
bot.polling()
