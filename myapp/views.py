from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.decorators import login_required
from .models import UploadedFile
from .forms import FileUploadForm
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import UserCreationSerializer


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token)
    }

def index(request):
    return render(request, 'index.html')

@api_view(['POST'])
def register(request):
    serializer = UserCreationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        tokens = get_tokens_for_user(user)
        return Response({'status': 1, 'message': '注册成功', 'tokens': tokens}, status=status.HTTP_201_CREATED)
    return Response({'status': 0, 'message': '注册失败'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_view(request):
    form = AuthenticationForm(request, data=request.data)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # Generate JWT tokens on successful login
            tokens = get_tokens_for_user(user)
            return Response({'status': 1, 'message': '登录成功', 'tokens': tokens}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 0, 'message': '用户名或密码错误'}, status=status.HTTP_400_BAD_REQUEST)
    return Response({'status': 0, 'message': '登录失败'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def logout_view(request):
    logout(request)
    return Response({'status': 1, 'message': '登出成功'}, status=status.HTTP_200_OK)

@api_view(['POST'])
@login_required
def dashboard(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = FileUploadForm()
    uploaded_files = UploadedFile.objects.all()
    return render(request, 'dashboard.html', {'form': form, 'uploaded_files': uploaded_files})

# Protect views using JWT authentication
@api_view(['GET'])
def protected_view(request):
    permission_classes = [IsAuthenticated]
    return Response({"message": "This is a protected view."}, status=status.HTTP_200_OK)