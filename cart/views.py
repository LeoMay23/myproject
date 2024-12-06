from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from purchased.models import PurchasedItem
from .models import CartItem
from product.models import Product
from .serializers import CartItemSerializer

def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.total_price() for item in cart_items)
    return render(request, 'cart/cart.html', {'cart_items': cart_items, 'total': total})


@api_view(['POST'])
@permission_classes([IsAuthenticated])  # Require authentication to add to cart
def add_to_cart(request):
    data = request.data
    product = get_object_or_404(Product, id=data['id'])
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)

    if not created:
        cart_item.quantity += 1
    cart_item.save()

    return Response({'status': 1, 'message': '加入购物车成功'}, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])  # Require authentication to remove from cart
def remove_from_cart(request):
    data = request.data
    cart_item = get_object_or_404(CartItem, id=data['id'], user=request.user)
    cart_item.delete()

    return Response({'status': 1, 'message': '从购物车移除成功'}, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_cart_items(request):
    cart_items = CartItem.objects.filter(user=request.user)
    serializer = CartItemSerializer(cart_items, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_cart_item_quantity(request):
    update_data = request.data.get('items', [])
    for data in update_data:
        cart_item = get_object_or_404(CartItem, id=data['id'], user=request.user)
        new_quantity = data.get('quantity')
        if cart_item is not None:
            if new_quantity is None:
                return Response({'status': 0, 'message': '无效的商品数量'}, status=status.HTTP_400_BAD_REQUEST)
            elif int(new_quantity) <= 0:
                cart_item.delete()
            else:
                cart_item.quantity = int(new_quantity)
                cart_item.save()

    return Response({'status': 1, 'message': '购物车商品数量更新成功'}, status=status.HTTP_200_OK)
