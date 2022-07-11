from distutils.command.upload import upload
from statistics import mode
from django.db import models

class Good(models.Model):
    name = models.TextField(verbose_name='Наименование товара')
    caption = models.TextField(verbose_name='Описание товара', blank=True, null=True, default='')
    cost = models.IntegerField(verbose_name='Цена товара', blank=True, null=True)
    picture = models.ImageField(verbose_name='Изображение товара', upload_to='uploads/good_images/', blank=True, null=True)

    def __str__(self):
        return self.name