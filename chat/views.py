from django.db.models import Q

from .models import ChatModel
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class ChatView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_id = request.user.id

        chats = ChatModel.objects.filter(Q(user_sender=user_id) | Q(user_receiver=user_id)).values()
        return Response(chats, status=status.HTTP_200_OK)
