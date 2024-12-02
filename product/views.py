from django.shortcuts import render, get_object_or_404
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Product
from .serializers import ProductSerializer

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product/product_detail.html', {'product': product})

class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'