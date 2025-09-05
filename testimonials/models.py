from django.db import models
from django.core.validators import MaxValueValidator

from clients.models import Client
from plans.models import Plan


class Testimonial(models.Model):
    """
    A Testimonial is a review of a client's experience with a plan.
    """
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    plan_id = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True)
    star_rating = models.IntegerField(
        validators=[MaxValueValidator(5)]  # Limits the value to a maximum of 100)
    )
    review_text = models.TextField()

    def __str__(self) -> str:
        return f"Testimonial: {self.review_text} 5-Star Rating: {self.star_rating}"
