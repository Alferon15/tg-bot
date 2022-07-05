import logging
import telebot

from telebot import types
from tg_bot.utils.bot_config import API_TOKEN, admin_id
from models import TGUser


logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

bot = telebot.TeleBot(API_TOKEN, parse_mode=None)


def process_webhook(body):
    json_obj = body.decode('UTF-8')
    update = types.Update.de_json(json_obj)
    user_id = update.message.from_user
    u = TGUser.objects.get_or_create(user_id)
    if not u.is_trusted:
        bot.send_message(user_id, 'Я тебя не знаю!')
    bot.send_message(admin_id, update)
    bot.send_message(admin_id, update.message)
    bot.send_message(admin_id, update.message.from_user)