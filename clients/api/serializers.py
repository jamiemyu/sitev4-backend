from rest_framework.serializers import ModelSerializer
from ..models import Client


class ClientsSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "enrollment_status",
        )
