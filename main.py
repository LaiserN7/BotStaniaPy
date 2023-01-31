import requests
from fastapi import FastAPI, Request
from infrastructure import Bot
import os
import logging
import telebot

app = FastAPI()
logging.getLogger().setLevel(logging.INFO)
# token = os.environ['BOT_TOKEN']
token = '5699281086:AAHjGw9zfFBe0PFIuGmAk7poTTczcWGfC4Y'
logging.info(f"current env token is : {os.environ['BOT_TOKEN']}")

# cur_url = os.environ['URL']

logging.info(f"current token is : {token}")
bot = Bot(api_token=token)
@bot.client.message_handler(commands=['start'])
def url(message):
    logging.info("kek")
    logging.info(message)
    bot.client.send_message(message.from_user.id, "Pic")


@app.on_event("startup")
async def on_startup():
    logging.info("Starting")


@app.get("/")
async def root():
    return {"message": f"Hello"}


@app.post("/update")
async def bot_webhook(update: telebot.types.Update):
    logging.log(update)
    # print(request.headers)
    # if request.headers.get('content-type') == 'application/json':
    #     json_string = request.body()
    #     # update = telebot.types.Update.de_json(json_string)
    #     logging.info(json_string)
    #     bot.client.process_new_messages(json_string)
    #     return ''

    await bot.client.process_new_updates(update)

# bot.client.remove_webhook()
# bot.client.set_webhook(f'{cur_url}update/ + {token}')

# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}
# bot.client.polling(none_stop=True, interval=0)
