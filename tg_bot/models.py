from django.db import models


# Create your models here.
class TGUser(models.Model):
    class Meta:
        ordering = ["tg_id"]
    
    tg_id = models.IntegerField()
    is_trusted = models.BooleanField(default=False)
    user_name = models.CharField(max_length=50, help_text="Enter user name")
    

    def __str__(self):
        return self.tg_id
    
    
class Printer(models.Model):
    class Meta:
        pass
    
    printer_name = models.CharField(max_length=100, help_text="")


    def __str__(self):
        return self.printer_name


class Cartridge(models.Model):
    class Meta:
        pass
    
    cartridge_name = models.CharField(max_length=100, help_text="")
    printers = models.ManyToManyField(Printer)


    def __str__(self):
        return self.cartridge_name