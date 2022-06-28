from django.shortcuts import render, HttpResponse
from tg_bot.utils.bot import bot
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
@csrf_exempt
async def webhook_process(request):
    if request.method == "POST":
        bot.send_message(100204219, 'webhook_process')
        print("Data received from Webhook is: ", request.body)
        return HttpResponse('POST')
    else:
        return HttpResponse('GET')