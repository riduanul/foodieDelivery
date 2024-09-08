from django.db import models
from user.models import CustomUser, Restaurant
from menu.models import MenuItem
# Create your models here.


PAYMENT_METHOD= [
    ('cash', 'cash'),
    ('card', 'card'),
]

class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    items = models.ManyToManyField(MenuItem, )
    payment_method = models.CharField(choices=PAYMENT_METHOD, max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)


    @property
    def total_price(self):
        total = sum(item.get_total_price() for item in self.orderitem_set.all())
        return total
    
    def __str__(self):
        return f"Order {self.id} by {self.user.first_name} at {self.restaurant.name}"


class OrderItem(models.Model):
    Order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_total_price(self):
        return self.menu_item.price * self.quantity
    
    def __str__(self):
        return f"{self.quantity} x {self.menu_item.name}"

