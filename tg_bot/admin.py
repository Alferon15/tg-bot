from django.contrib import admin
from tg_bot.models import TGUser, Printer, Cartridge

# Register your models here.
@admin.register(TGUser)
class TGUserAdmin(admin.ModelAdmin):
    pass


@admin.register(Printer)
class PrinterAdmin(admin.ModelAdmin):
    pass


@admin.register(Cartridge)
class CartridgeAdmin(admin.ModelAdmin):
    pass