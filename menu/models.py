from django.db import models
from user.models import Restaurant
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    
    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
        
    def __str__(self):
        return self.name



class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete = models.CASCADE )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)


    def __str__(self):
        return self.name 