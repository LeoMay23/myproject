from purchased import views
from django.urls import path

urlpatterns = [
    path('api/purchased_items/', views.get_purchased_items, name='purchased'),
    path('api/purchased_item/<int:pk>/', views.get_purchased_item, name='purchased_item'),
    path('api/checkout/', views.checkout, name='checkout'),
]