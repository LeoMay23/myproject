from itertools import product

from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from cart.models import CartItem
from .models import PurchasedItem
from .serializers import PurchasedItemSerializer
from product.models import Product

# View to retrieve all purchased items for the logged-in user
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_purchased_items(request):
    purchased_items = PurchasedItem.objects.filter(user=request.user)
    serializer = PurchasedItemSerializer(purchased_items, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# View to retrieve a single purchased item by ID
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_purchased_item(request, pk):
    try:
        purchased_item = PurchasedItem.objects.get(id=pk, user=request.user)
    except PurchasedItem.DoesNotExist:
        return Response({'detail': 'Item not found.'}, status=status.HTTP_404_NOT_FOUND)

    serializer = PurchasedItemSerializer(purchased_item)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])  # 需要认证用户才能结算
def checkout_cart(request):
    # 获取前端传递的商品 ID 和数量
    cart_data = request.data.get('items', [])
    if not cart_data:
        return Response({'status': 0, 'message': '没有选择商品进行结算'}, status=status.HTTP_400_BAD_REQUEST)

    purchased_items = []

    # 处理选中的商品
    for data in cart_data:
        product_id = data.get('id')
        quantity = data.get('quantity')

        # 查找购物车中的商品
        cart_item = CartItem.objects.filter(user=request.user, product_id=product_id).first()

        if not cart_item:
            return Response({'status': 0, 'message': f'商品 {product_id} 不在购物车中'},
                            status=status.HTTP_400_BAD_REQUEST)

        if cart_item.quantity < quantity:
            return Response({'status': 0, 'message': f'购物车中 {cart_item.product.name} 的数量不足'},
                            status=status.HTTP_400_BAD_REQUEST)

        # 创建购买记录
        purchased_items.append(PurchasedItem(
            user=request.user,
            product=cart_item.product,
            quantity=quantity
        ))

        # 更新购物车中的商品数量
        cart_item.quantity -= quantity
        if cart_item.quantity == 0:
            cart_item.delete()
        else:
            cart_item.save()

    # 批量创建购买记录
    PurchasedItem.objects.bulk_create(purchased_items)

    return Response({'status': 1, 'message': '结算成功'}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])  # 需要认证用户才能结算
def checkout_item(request):
    # 获取前端传递的商品 ID 和数量
    item_id = request.data.get('id')
    product = get_object_or_404(Product, pk=item_id)
    if not product:
        return Response({'status': 0, 'message': '没有选择商品进行结算'}, status=status.HTTP_400_BAD_REQUEST)

    # 处理选中的商品
    purchased_items = []
    purchased_items.append(PurchasedItem(
        user=request.user,
        product=product,
        quantity= 1
    ))

    # 批量创建购买记录
    PurchasedItem.objects.bulk_create(purchased_items)

    return Response({'status': 1, 'message': '结算成功'}, status=status.HTTP_200_OK)



