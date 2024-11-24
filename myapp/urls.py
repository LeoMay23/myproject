# myapp/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),  # 首页路由
    path('register/', views.register, name='register'),  # 用户注册
    path('login/', auth_views.LoginView.as_view(), name='login'),  # 用户登录
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # 用户登出
    path('dashboard/', views.dashboard, name='dashboard'),  # 用户主页路由
]

