from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from product.models import Product

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} - {self.product.name} x {self.quantity}"

    def total_price(self):
        return self.quantity * self.product.price

