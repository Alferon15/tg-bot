from statistics import mode
from typing_extensions import Required
from django.db import models
from django.shortcuts import reverse
from django.utils.safestring import mark_safe

class Good(models.Model):
    name = models.TextField(verbose_name='Наименование товара')
    caption = models.TextField(verbose_name='Описание товара', blank=True, null=True, default='')
    cost = models.IntegerField(verbose_name='Цена товара', blank=True, null=True)


    def get_absolute_url(self):
        return reverse('catalog:detail', kwargs={'pk': self.pk})
    

    def __str__(self):
        return self.name


    def image(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.picture.url))


class GoodImage(models.Model):
    good = models.ForeignKey(Good, related_name='images', on_delete=models.CASCADE)
    number = models.IntegerField(verbose_name='Номер изображения', blank=False, null=False, unique=True)
    image = models.ImageField(verbose_name='Изображение товара', upload_to='good_images/', blank=True, null=True)