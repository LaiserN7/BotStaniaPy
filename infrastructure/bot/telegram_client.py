import telebot
from telebot.async_telebot import AsyncTeleBot

class Bot:
    def __init__(self, api_token):
        self.__token__: str = api_token
        self.client = telebot.TeleBot(api_token)

