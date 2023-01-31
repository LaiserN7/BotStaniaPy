from fastapi import FastAPI
from infrastructure import Bot
import os
import logging

app = FastAPI()
logging.getLogger().setLevel(logging.INFO)
token = os.environ['BOT_TOKEN']
cur_url = os.environ['URL']
logging.info(f"current token is : {os.environ['BOT_TOKEN']}")
bot = Bot(api_token=token)
print("via print")
print(f"current token is : {os.environ['BOT_TOKEN']}")
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
    return {"message": f"Hello {bot.client.token}"}


@app.post("update")
async def bot_webhook(update: dict):
    await bot.client.process_new_updates(dict)

bot.client.remove_webhook()
bot.client.set_webhook(f'{cur_url}update/ + {token}')

# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}
# bot.client.polling(none_stop=True, interval=0)
