from rest_framework.serializers import ModelSerializer
from ..models import Plan

class PlansSerializer(ModelSerializer):
    class Meta:
        model = Plan
        fields = ('id', 'name', 'description')