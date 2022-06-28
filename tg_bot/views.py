import logging

from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from asgiref.sync import async_to_sync

from tg_bot.utils.bot import bot_to_admin


@method_decorator(csrf_exempt, name='dispatch')
class WebhookProcess(View):
    def get(self, request, *args, **kwargs):  # for debug
        return JsonResponse({"ok": "Get request received! But nothing done"})
    def post(self, request, *args, **kwargs):
        logging.info('webhook_process!!!')
        logging.info(request)
        async_to_sync(bot_to_admin())
        return JsonResponse({"ok": "POST request processed"})
