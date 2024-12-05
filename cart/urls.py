from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_view, name='cart_view'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('api/add/', views.add_to_cart, name='api_add_to_cart'),
    path('api/remove/', views.remove_from_cart, name='api_remove_from_cart'),
    path('api/items/', views.get_cart_items, name='api_get_cart_items'),
    path('api/update/', views.update_cart_item_quantity, name='update_cart_item_quantity'),
]