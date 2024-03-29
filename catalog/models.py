from django.db import models
from django.shortcuts import reverse
from django.utils.safestring import mark_safe


class Good(models.Model):
    name = models.TextField(verbose_name='Наименование товара')
    caption = models.TextField(verbose_name='Описание товара', blank=True, null=True, default='')
    cost = models.IntegerField(verbose_name='Цена товара', blank=True, null=True)
    image_main = models.ImageField(verbose_name='Изображение товара', upload_to='good_images/', blank=True, null=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('catalog:detail', kwargs={'pk': self.pk})
    
    def image_picture(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image_main.url))


class GoodImage(models.Model):
    good = models.ForeignKey(Good, related_name='add_images', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Изображение товара', upload_to='good_images/', blank=True, null=True)

    def image_picture(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
