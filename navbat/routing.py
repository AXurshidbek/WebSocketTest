from django.urls import path
from .consumers import *

websocket_urlpatterns=[
    path("person/", PersonConsumer.as_asgi())
]