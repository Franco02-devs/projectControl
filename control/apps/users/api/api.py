from rest_framework.views import APIView
from rest_framework.response import Response
from apps.users.models import User
from apps.users.api.serializers import UserSerializer
from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def user_api_view(request):
    if request.method == "GET":
        users=User.objects.all()
        users_serializer = UserSerializer(users,many=True)
        return Response(users_serializer.data)
        