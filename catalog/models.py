from django.db import models

class Good(models.Model):
    name = models.TextField(verbose_name='Наменование товара')
