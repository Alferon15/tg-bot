from pyexpat import model
from django.contrib import admin
from catalog.models import Good, GoodImage

# Register your models here.


class GoodImageInline(admin.TabularInline):
    model = GoodImage
    extra = 0 
    
@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'image_picture', 'cost']
    list_display_links = ['name']
    inlines = [ GoodImageInline ]


@admin.register(GoodImage)
class GoodImageAdmin(admin.ModelAdmin):
    list_display = ['image_pucture']
    inlines = [GoodImageInline]
