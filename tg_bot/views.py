import logging

from django.views import View
from django.http import JsonResponse
from tg_bot.utils.bot import bot_to_admin
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')
class WebhookProcess(View):
    def get(self, request, *args, **kwargs):  # for debug
        return JsonResponse({"ok": "Get request received! But nothing done"})
    def post(self, request, *args, **kwargs):
        logging.warning('webhook_process!!!')
        logging.warning(request)
        bot_to_admin()
        return JsonResponse({"ok": "POST request processed"})
