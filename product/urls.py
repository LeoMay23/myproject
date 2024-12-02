from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('api/', views.ProductListView.as_view(), name='api_product_list'),
    path('api/<int:id>/', views.ProductDetailView.as_view(), name='api_product_detail'),
]