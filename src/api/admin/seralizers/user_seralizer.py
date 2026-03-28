from rest_framework.serializers import ModelSerializer
from apps.users.models import User



class UserSeralizers(ModelSerializer):

    class Meta:

        model = User
        fields = ['id', "first_name", "last_name", "email"]


