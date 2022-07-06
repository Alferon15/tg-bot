from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from tg_bot.utils.bot import process_webhook


@method_decorator(csrf_exempt, name='dispatch')
class WebhookProcess(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse({"ok": "Get request received! But nothing done"})
    def post(self, request, *args, **kwargs):
        process_webhook(request.body)
        return JsonResponse({"ok": "POST request processed"})
