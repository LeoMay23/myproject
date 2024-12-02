from rest_framework import serializers

from product.models import Product
from product.serializers import ProductSerializer
from .models import CartItem

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = CartItem
        fields = ['id', 'user', 'product', 'quantity']