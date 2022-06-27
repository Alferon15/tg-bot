from django.shortcuts import render
from tg_bot.utils.bot import bot


# Create your views here.
def webhook_process(request):
    bot.send_message(100204219, 'webhook_process')
    return render(request)