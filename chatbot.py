#!C:\python27\python.exe
# -*- coding: utf-8 -*-
#print('Content-type:text/html\n')
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os

def chat():
    bot = ChatBot("Bot")
    bot.set_trainer(ListTrainer)

    for files in os.listdir('C:/Users\Anmol\AppData\Roaming\Python\Python36\site-packages\chatterbot_corpus\data\english/'):
        data = open('C:/Users\Anmol\AppData\Roaming\Python\Python36\site-packages\chatterbot_corpus\data\english/' + files,'r').readlines()
        bot.train(data)

    while True:
        message = input("you: ")
        if message.strip() != 'Bye':
            reply = bot.get_response(message)
            print('chatbot : ',reply)
        if message.strip() == 'Bye':
            print('Chatbot : Take care')
            break

chat()