# myapp/signals.py
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.conf import settings

@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        send_mail(
            '欢迎注册',
            '感谢注册，我们很高兴为您提供服务。',
            settings.DEFAULT_FROM_EMAIL,
            [instance.email],
            fail_silently=False,
        )

