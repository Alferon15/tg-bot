import logging
from venv import create
import telebot

from telebot import types
from tg_bot.utils.bot_config import API_TOKEN, admin_id
from tg_bot.models import TGUser


logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

bot = telebot.TeleBot(API_TOKEN, parse_mode=None)


def process_webhook(body):
    json_obj = body.decode('UTF-8')
    update = types.Update.de_json(json_obj)
    userid = update.message.from_user.id
    username = update.message.from_user.username
    u, created = TGUser.objects.get_or_create(pk=userid)
    if created:
        u.user_name = username
        u.save()
        bot.send_message(userid, 'Я добавил тебя в свой список!')
    bot.send_message(userid, 'Тебе можно доверять!' if u.is_trusted else 'Я тебя не знаю!')
    bot.send_message(admin_id, update.message)