import logging
import telebot

from telebot import types
from tg_bot.utils.bot_config import API_TOKEN, admin_id


logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

bot = telebot.TeleBot(API_TOKEN, parse_mode=None)


def process_webhook(body):
    json_obj = body.decode('UTF-8')
    update = types.Update.de_json(json_obj)
    bot.send_message(admin_id, update.update_id)
    bot.send_message(admin_id, update.message.entities)
    bot.send_message(admin_id, update.message.from_user)
    bot.send_message(admin_id, update.message)
    bot.send_message(admin_id, update.message.date)