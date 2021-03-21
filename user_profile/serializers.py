from rest_framework.serializers import ModelSerializer

from .models import UserProfile


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'name', 'surname', 'age', 'avatar']
