from rest_framework import viewsets
from client.models import Client
from client.api.serializer import ClientSerializer


class ClintViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
