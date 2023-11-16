from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_notifications = models.BooleanField(default=False)
    currency = models.CharField(max_length=10)
    want_subcategory = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


class TelegramBucket(models.Model):
    user_chat_id = models.CharField(max_length=10)
    access_code = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)


class UserTelegram(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telegram_bucket = models.OneToOneField(TelegramBucket, on_delete=models.CASCADE)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
