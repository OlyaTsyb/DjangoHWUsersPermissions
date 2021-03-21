from rest_framework.serializers import ModelSerializer, ValidationError
from django.contrib.auth import get_user_model

from user_profile.serializers import ProfileSerializer

UserModel = get_user_model()


class UserSerializer(ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = UserModel
        fields = ['id', 'email', 'username', 'password', 'is_superuser', 'is_staff', 'is_active', 'profile']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validate_data):
        try:
            user = UserModel.objects.create_user(**validate_data)
        except ValueError as err:
            raise ValidationError(err)
        return user
