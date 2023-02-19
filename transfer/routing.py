from django.urls import re_path
from .consumers import Chat

websocket_patterns = [
    re_path(r"(?P<chat_name>\w+)/", Chat.as_asgi())
]
