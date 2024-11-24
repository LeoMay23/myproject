# Create your views here.
# myapp/views.py
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from .forms import CustomUserCreationForm, CustomUserChangeForm  # 导入表单
from django.contrib.auth.decorators import login_required

def index(request):  # 首页
    return render(request, 'index.html')  # 渲染首页模板

def login_view(request):  # 登录
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # 登录逻辑
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # 如果用户认证成功，登录并重定向
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')  # 登录成功后重定向到首页
            else:
                form.add_error(None, '用户名或密码错误')
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):  # 登出
    logout(request)
    return redirect('index')  # 登出后重定向到首页页面

def register(request):  # 注册
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # 保存新用户
            return redirect('login')  # 注册成功后跳转到登录页面
    else:
        form = CustomUserCreationForm()  # 显示空的注册表单
    return render(request, 'registration/register.html', {'form': form})

# 使用 login_required 装饰器确保只有已登录的用户可以访问此视图

from django.shortcuts import render, redirect
from .forms import FileUploadForm
from .models import UploadedFile

@login_required
def dashboard(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)  # 接收文件数据
        if form.is_valid():
            form.save()  # 保存文件到数据库和上传目录
            return redirect('dashboard')  # 上传成功后刷新页面
    else:
        form = FileUploadForm()

        # 获取已上传的文件列表
    uploaded_files = UploadedFile.objects.all()

    return render(request, 'dashboard.html', {'form': form, 'uploaded_files': uploaded_files})
#    return render(request, 'dashboard.html')  # 渲染用户主页模板
