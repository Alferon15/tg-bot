import logging
import telebot
import json

from tg_bot.utils.bot_config import API_TOKEN, admin_id


WEBAPP_HOST = 'http://alferon15.pythonanywhere.com' 
WEBAPP_PORT = 80

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

bot = telebot.TeleBot(API_TOKEN, parse_mode=None)


def process_webhook(body):
    json_obj = json.loads(body)
    bot.send_message(admin_id, json_obj)