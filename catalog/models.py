from statistics import mode
from django.db import models
from django.shortcuts import reverse
from django.utils.safestring import mark_safe

class Good(models.Model):
    name = models.TextField(verbose_name='Наименование товара')
    caption = models.TextField(verbose_name='Описание товара', blank=True, null=True, default='')
    cost = models.IntegerField(verbose_name='Цена товара', blank=True, null=True)
    picture = models.ImageField(verbose_name='Изображение товара', upload_to='uploads/good_images/', blank=True, null=True)


    def get_absolute_url(self):
        return reverse('catalog:detail', kwargs={'pk': self.pk})
    

    def __str__(self):
        return self.name


    def picture_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.picture.url))
        
    picture_tag.short_description = 'Image'