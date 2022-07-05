from django.contrib import admin
from tg_bot.models import TGUser, Printers, Cartridges

# Register your models here.
@admin.register(TGUser)
class TGUserAdmin(admin.ModelAdmin):
    pass


@admin.register(Printers)
class PrintersAdmin(admin.ModelAdmin):
    pass


@admin.register(Cartridges)
class CartridgesAdmin(admin.ModelAdmin):
    pass