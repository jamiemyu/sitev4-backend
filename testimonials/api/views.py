from rest_framework.viewsets import ModelViewSet

from ..models import Testimonial
from .serializers import TestimonialsSerializer


class TestimonialsViewSet(ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialsSerializer