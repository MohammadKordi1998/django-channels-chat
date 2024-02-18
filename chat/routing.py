from django.urls import path
from .consumer import ChatConsumer

websocket_urlpatterns = [
    path('ws/chat/<username>/<token>/', ChatConsumer.as_asgi())
]
