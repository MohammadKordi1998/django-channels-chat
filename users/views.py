from .models import UsersModel
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = UsersModel.objects.all().values('username')
        return Response(users)


class AuthView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        username = request.user.username
        user_id = request.user.id
        object_user = dict(
            id=user_id,
            username=username,
        )
        return Response(object_user, status=status.HTTP_200_OK)
