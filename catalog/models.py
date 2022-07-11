from django.db import models

class Good(models.Model):
    name = models.TextField(verbose_name='Наменование товара')
    caption = models.TextField(verbose_name='Описание товара')

    def __str__(self):
        return self.name