from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_view, name='cart_view'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('purchased/', views.purchased_items, name='purchased_items'),
    path('api/add/', views.add_to_cart, name='api_add_to_cart'),
    path('api/remove/', views.remove_from_cart, name='api_remove_from_cart'),
    path('api/items/', views.get_cart_items, name='api_get_cart_items'),
]