from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from ..models import Client
from .serializers import ClientsSerializer


class ClientsViewSet(ModelViewSet):
    """
    A ModelViewSet for a Client.
    """
    queryset = Client.objects.all()
    serializer_class = ClientsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name'] # Specify fields to search
