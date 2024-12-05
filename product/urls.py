from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.product_list, name='api_product_list'),
    path('api/detail/<int:id>/', views.product_detail, name='api_product_detail'),
]