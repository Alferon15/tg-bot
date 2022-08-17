from django.contrib import admin
from catalog.models import Good, GoodImage

# Register your models here.


class GoodImageInline(admin.StackedInline):
    model = GoodImage


@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'cost', 'images']
    list_display_links = ['name']
    inlines = [ GoodImageInline ]


@admin.register(GoodImage)
class GoodImageAdmin(admin.ModelAdmin):
    list_display = ['good', 'number', 'image_pucture']
