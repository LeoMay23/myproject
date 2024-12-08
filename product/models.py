from django.db import models

# Create your models here.
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class ProductDetail(models.Model):
    product = models.OneToOneField(Product, related_name='detailDescription', on_delete=models.CASCADE)
    detail_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Detail for {self.product.name}"

class ProductKeyword(models.Model):
    product = models.ForeignKey(Product, related_name='keywords', on_delete=models.CASCADE)
    keyword = models.CharField(max_length=100)

    def __str__(self):
        return self.keyword

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return f"Image for {self.product.name}"

class ProductComment(models.Model):
    product = models.ForeignKey(Product, related_name='comments', on_delete=models.CASCADE)
    username = models.CharField(max_length=100, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.comment