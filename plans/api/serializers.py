from rest_framework.serializers import ModelSerializer
from ..models import Plan

class PlansSerializer(ModelSerializer):
    """
    A serializer for the Plan model.
    """
    class Meta:
        """
        Configures how the serializer interacts with the Plan model.
        """
        model = Plan
        fields = '__all__'