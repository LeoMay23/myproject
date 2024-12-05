# myapp/serializers.py
from rest_framework import serializers

from myproject.settings import BASE_DIR
from .models import Product, ProductImage, ProductDetail, ProductKeyword


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image']

class ProductDetailDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model =  ProductDetail
        fields = ['detail_description']

class ProductKeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductKeyword
        fields = ['keyword']

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True)
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock', 'images']

class ProductDetailSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many= True)
    detailDescription = ProductDetailDescriptionSerializer(many = False)
    keywords = ProductKeywordSerializer(many= True)
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock', 'images', 'detailDescription', 'keywords']