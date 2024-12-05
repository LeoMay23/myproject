import django_filters
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Product
from .serializers import ProductSerializer, ProductDetailSerializer
from rest_framework import status
from rest_framework import viewsets, filters

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def product_detail(request , id):
    if request.method == 'GET':
        data = request.data
        product = get_object_or_404(Product, id=id)
        if product is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductDetailSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
