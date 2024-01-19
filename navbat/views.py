from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from channels.layers import get_channel_layer
from asgiref.sync import sync_to_async, async_to_sync

from .serializers import *
from .models import *
from .consumers import *

class PersonPostAPI(APIView):
    # def get(self,request):
    #     persons=Person.objects.all()
    #     serializer=PersonSerializer(persons, many=True)
    #
    #     return Response()
    #

    def post(self, request):
        serializer=PersonSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            channel_layer=get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                "person_group",
                {
                    "type": "add_new_person"
                }
            )
            return Response(serializer.data)
        return Response(serializer.errors)
