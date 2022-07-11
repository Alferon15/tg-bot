from django.contrib import admin
from catalog.models import Good

# Register your models here.
@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    pass