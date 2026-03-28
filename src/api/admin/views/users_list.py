
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.users.models import User
from api.admin.seralizers.user_seralizer import UserSeralizers



class UserListApiView(APIView):

    def get(self, request):
        users = User.objects.all()
        user_ser = UserSeralizers(users, many=True)
        data = {
            "message": "ok",
            "status": "backenddan salomlar",
            "users": user_ser.data
        }
        return Response(data, status=status.HTTP_200_OK)
    
