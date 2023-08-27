from django.db import models

# Create your models here.
class Product5(models.Model):
    itemname = models.CharField(max_length=45)
    itemprice =models.FloatField(default=0)
    itemimage= models.ImageField(upload_to='media')

    def __str__(self):
        return self.itemname
    