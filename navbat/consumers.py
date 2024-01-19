from channels.generic.websocket import AsyncWebsocketConsumer
import json
from asgiref.sync import sync_to_async
from .serializers import *


class PersonConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        async def connect(self):
            await self.accept()
            await self.channel_layer.group_add("person_group", self.channel_name)
            await self.send_initial_person_list()

        async def send_initial_person_list(self):
            person_list=await self.get_person_list()
            await self.send(text_data=json.dumps(person_list))

        @sync_to_async
        def get_person_list(self):
            persons=Person.objects.all()
            serializer=PersonSerializer(persons, many=True)
            return serializer.data


        async def add_new_person(self,event):
            await self.send_initial_person_list()

        async def disconnect(self, code):
            await self.channel_layer.group_discard("person_group", self.channel_name)