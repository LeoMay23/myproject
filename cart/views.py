from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import CartItem, PurchasedItem
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


# API view to remove an item from the cart
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])  # Require authentication to remove from cart
def remove_from_cart(request):
    data = request.data
    cart_item = get_object_or_404(CartItem, id=data['id'], user=request.user)
    cart_item.delete()

    return Response({'status': 1, 'message': '从购物车移除成功'}, status=status.HTTP_200_OK)


# API view to retrieve the user's cart items
@api_view(['GET'])
@permission_classes([IsAuthenticated])  # Require authentication to view cart items
def get_cart_items(request):
    cart_items = CartItem.objects.filter(user=request.user)
    serializer = CartItemSerializer(cart_items, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# Checkout function to process the user's purchase and empty their cart
@api_view(['POST'])
@permission_classes([IsAuthenticated])  # Protect this view to ensure only authenticated users can checkout
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    if not cart_items.exists():
        return Response({'status': 0, 'message': '购物车为空，无法结账'}, status=status.HTTP_400_BAD_REQUEST)

    # Process the checkout
    for item in cart_items:
        PurchasedItem.objects.create(
            user=request.user,
            product=item.product,
            quantity=item.quantity
        )
        item.delete()  # Remove the item from the cart after purchase

    return redirect('purchased_items')  # Redirect to the purchased items view


# View to display the purchased items
def purchased_items(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Ensure that the user is authenticated before accessing this page

    items = PurchasedItem.objects.filter(user=request.user)
    return render(request, 'cart/purchased_items.html', {'items': items})