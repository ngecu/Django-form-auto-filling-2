from django.db import models

# Create your models here.
class Shoe(models.Model):
    title = models.CharField(max_length=200,null=True,blank=True)
    price = models.CharField(max_length=200,null=True,blank=True)
    image = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Shoes"


