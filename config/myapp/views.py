from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializer import ServerSerializer
from .serializer_status import ServerSerializerStatus
from .models import Server

class ServerViewSet(generics.ListAPIView):

    queryset = Server.objects.all()
    serializer_class = ServerSerializer

class ServerAddView(generics.CreateAPIView):

    queryset = Server.objects.all()
    serializer_class = ServerSerializer

class ServerDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Server.objects.all()
    serializer_class = ServerSerializer

class ServerViewStatus(generics.ListAPIView):

    queryset = Server.objects.all()
    serializer_class = ServerSerializerStatus

