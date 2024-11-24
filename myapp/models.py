# myapp/models.py
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title


# Create your models here.

#文件上传
from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')  # 指定文件存储路径
    uploaded_at = models.DateTimeField(auto_now_add=True)  # 记录上传时间

    objects = models.Manager()  # 确保使用默认管理器

    def __str__(self):
        return self.file.name
