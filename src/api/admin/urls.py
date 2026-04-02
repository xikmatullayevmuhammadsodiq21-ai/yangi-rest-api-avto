
from django.urls import path
from api.admin.views.users_list import UserListApiView
from api.admin.views.auto_cobald import AutoCobaldApiView
from api.admin.views.auto_tiko import AutoTikoApiView
from api.admin.views.auto_matiz import AutoMatizApiView
from api.admin.views.auto_tracker import AutoTrackerApiView
from api.admin.views.auto_malibu import AutoMalibuApiView
from api.admin.views.auto_spark import AutoSparkApiView
from api.admin.views.auto_bwd import AutoBwdApiView


urlpatterns = [
    path("user/list/", UserListApiView.as_view()),
    path("auto/tiko/", AutoTikoApiView.as_view()),
    path("auto/cobald/", AutoCobaldApiView.as_view()),
    path("auto/matiz/", AutoMatizApiView.as_view()),
    path("auto/tracker/", AutoTrackerApiView.as_view()),
    path("auto/malibu/", AutoMalibuApiView.as_view()),
    path("auto/spark/", AutoSparkApiView.as_view()),
    path("auto/bwd/", AutoBwdApiView.as_view()),
]

