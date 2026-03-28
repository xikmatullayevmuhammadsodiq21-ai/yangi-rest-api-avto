
from django.urls import path
from api.admin.views.users_list import UserListApiView


urlpatterns = [
    path("user/list/", UserListApiView.as_view()),
]

