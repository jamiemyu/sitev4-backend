from rest_framework.viewsets import ModelViewSet

from ..models import Plan
from .serializers import PlansSerializer


class PlansViewSet(ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlansSerializer
