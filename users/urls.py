from django.urls import path

from users.views import UserGetSelfInfo, AddProfile, ReadUpdateDelete

urlpatterns = [
    path('', UserGetSelfInfo.as_view(), name='users_list_create'),
    path('/<int:pk>/profile', AddProfile.as_view(), name='users_add_profile'),
    path('/<int:pk>', ReadUpdateDelete.as_view(), name='delete_permission_up_by_is_admin')

]
