from rest_framework import serializers
from .models import PurchasedItem

class PurchasedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchasedItem
        fields = ['id', 'user', 'product', 'quantity', 'purchase_date']

