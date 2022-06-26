from django.shortcuts import render
from tg_bot.utils.bot import bot_echo

# Create your views here.
def webhook_process(request):
    bot_echo('test')
    return render(request)