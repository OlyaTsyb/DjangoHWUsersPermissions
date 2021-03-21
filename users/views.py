from django.contrib.auth import get_user_model
from rest_framework.generics import ListCreateAPIView, CreateAPIView, get_object_or_404, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from user_profile.serializers import ProfileSerializer
from users.serializers import UserSerializer

UserModel = get_user_model()


class UserGetSelfInfo(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        self.request.query_params.get('pk')
        pk = self.request.user.pk
        queryset = UserModel.objects.filter(pk__exact=pk)
        return queryset


class AddProfile(CreateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        print(self.request.user)
        pk = self.kwargs.get('pk')
        user = get_object_or_404(UserModel, pk=pk)
        serializer.save(user=user)


class ReadUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def perform_update(self, serializer):
        pk = self.kwargs.get('pk')
        user = get_object_or_404(UserModel, pk=pk)
        serializer.save(user=user)
