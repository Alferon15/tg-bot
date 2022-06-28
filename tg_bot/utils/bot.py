import logging

from aiogram import Bot, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.webhook import SendMessage
from aiogram.utils.executor import start_webhook
from tg_bot.utils.bot_config import API_TOKEN, WEBHOOK_URL


# webserver settings
WEBAPP_HOST = 'http://alferon15.pythonanywhere.com'  # or ip
WEBAPP_PORT = 80

logging.basicConfig(
    filename='debug.log',
    level=logging.DEBUG,
)

logging.warning('bot started!')

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

@dp.message_handler(commands=['test','start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, "test message") #like this
    #await message.answer("test message") 
    #or like this

@dp.message_handler()
async def bot_echo(message: types.Message):
    # Regular request
    # await bot.send_message(message.chat.id, message.text)

    # or reply INTO webhook
    return SendMessage(message.chat.id, message.text)

@dp.message_handler()
async def bot_to_admin():
    return SendMessage(100204219, 'bot_to_admin')


async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)
    # insert code here to run it after start


async def on_shutdown(dp):
    logging.warning('Shutting down..')

    # insert code here to run it before shutdown

    # Remove webhook (not acceptable in some cases)
    await bot.delete_webhook()

    # Close DB connection (if used)
    await dp.storage.close()
    await dp.storage.wait_closed()

    logging.warning('Bye!')


if __name__ == '__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_URL,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )