from rest_framework.serializers import ModelSerializer
from ..models import Client


class ClientsSerializer(ModelSerializer):
    """
    A serializer for the Client model.
    """
    class Meta:
        """
        Configures how the serializer interacts with the Client model.
        """
        model = Client
        fields = '__all__'
