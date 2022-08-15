from django.contrib import admin
from catalog.models import Good

# Register your models here.
@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'cost')
    list_display_links = ('id', 'name')