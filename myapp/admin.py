from django.contrib import admin
# Register your models here.
# myapp/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class CustomUserAdmin(UserAdmin):
    # 在列表视图中添加显示的字段
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')

    # 配置哪些字段可以编辑
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2')}
        ),
    )

# 注册自定义的 UserAdmin
admin.site.unregister(User)  # 先取消注册默认的 User
admin.site.register(User, CustomUserAdmin)

#CustomUserAdmin 用来定制用户模型在 Admin 界面中的显示方式。通过 list_display 和 fieldsets，可以控制用户数据在后台如何展示、编辑。