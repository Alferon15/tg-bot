from django.contrib import admin
from catalog.models import Good, GoodImage

# Register your models here.
@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cost')
    list_display_links = ('id', 'name')


class GoodImageInline(admin.TabularInline):
    model = GoodImage
    extra = 3


class PropertyAdmin(admin.ModelAdmin):
    inlines = [ GoodImageInline, ]
