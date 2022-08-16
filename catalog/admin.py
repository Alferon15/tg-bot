from django.contrib import admin
from catalog.models import Good, GoodImage

# Register your models here.
@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'cost']
    list_display_links = ['id', 'name']


@admin.register(GoodImage)
class GoodImageAdmin(admin.ModelAdmin):
    list_display = ['number', 'image']


class GoodImageInline(admin.TabularInline):
    model = GoodImage
    extra = 3


class PropertyAdmin(admin.ModelAdmin):
    inlines = [ GoodImageInline, ]
