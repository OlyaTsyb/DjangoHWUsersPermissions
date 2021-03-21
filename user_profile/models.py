from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


def to_upload(instance, filename):
    return f'{instance.user.email}/avatars/{filename}'


class UserProfile(models.Model):
    class Meta:
        db_table = 'profile'

    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    age = models.IntegerField()
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to=to_upload)
