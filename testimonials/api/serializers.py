from rest_framework.serializers import ModelSerializer
from ..models import Testimonial


class TestimonialsSerializer(ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ("id", "client_id", "plan_id", "star_rating", "review_text")
