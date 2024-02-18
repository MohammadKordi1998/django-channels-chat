import json
import requests
from chat.models import ChatModel
from users.models import UsersModel
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        token = self.scope["url_route"]["kwargs"]['token']
        self.username = self.scope["url_route"]["kwargs"]["username"]

        # Start check username
        self.user_receiver = UsersModel.objects.filter(username=self.username).first()
        if not self.user_receiver:
            self.close()
        # End check username

        # Start Authorization
        ip = self.scope['server'][0]
        port = self.scope['server'][1]
        url = f'http://{ip}:{port}/users/auth/'
        header = {'Authorization': f'Bearer {token}'}
        self.auth = requests.get(url, headers=header)
        # End Authorization

        if self.auth.status_code == 200:
            self.auth = self.auth.json()

            self.room_group_name = f"chat_{self.username}"

            # Join room group
            async_to_sync(self.channel_layer.group_add)(
                self.room_group_name, self.channel_name
            )

            self.accept()
        else:
            self.close()

    def disconnect(self, close_code):
        self.close()

    # Receive message from WebSocket
    def receive(self, text_data=None, bytes_data=None):
        if text_data:
            ChatModel.objects.create(
                text=str(text_data),
                user_sender_id=self.auth['id'],
                user_receiver_id=self.user_receiver.id,
            )

            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name, {
                    "type": "chat.message",
                    "message": text_data
                }
            )

    def chat_message(self, event):
        message = event["message"]
        self.send(
            text_data=json.dumps({
                'message': message,
                'receiver': str(self.username),
                'sender': str(self.auth['username'])
            })
        )
