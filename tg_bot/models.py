from django.db import models

# Create your models here.
class TGUser(models.Model):
    class Meta:
        ordering = ["user_name"]
    
    tg_id = models.IntegerField()
    ally = models.BooleanField()
    user_name = models.CharField(max_length=50, help_text="Enter user name")
    
    
    
    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.field_name
    
    
class Printers(models.Model):
    class Meta:
        pass
    
    printer_name = models.CharField(max_lenght=100, help_text="")


class Cartridges(models.Model):
    class Meta:
        pass
    
    cartridge_name = models.CharField(max_lenght=100, help_text="")
    printers = models.ManyToManyField(Printers)