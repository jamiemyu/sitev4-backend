from rest_framework.viewsets import ModelViewSet

from ..models import Client
from .serializers import ClientsSerializer


class ClientsViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientsSerializer
