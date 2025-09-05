from rest_framework.serializers import ModelSerializer
from ..models import Testimonial


class TestimonialsSerializer(ModelSerializer):
    """
    A serializer for the Testimonial model.
    """
    class Meta:
        """
        Configures how the serializer interacts with the Testimonial model.
        """
        model = Testimonial
        fields = '__all__'