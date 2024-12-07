from rest_framework import serializers
from .models import PurchasedItem
from product.serializers import ProductSerializer

class PurchasedItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = PurchasedItem
        fields = ['id', 'user', 'product', 'quantity', 'purchase_date']

