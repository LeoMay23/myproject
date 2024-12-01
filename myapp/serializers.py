from django.contrib.auth.models import User
from rest_framework import serializers

class UserCreationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        # 使用 create_user 方法来确保密码哈希处理
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
