from django.db import models
from django.core.validators import MaxValueValidator

from clients.models import Client
from plans.models import Plan

# Create your models here.


class Testimonial(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    plan_id = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True)
    star_rating = models.IntegerField(
        validators=[MaxValueValidator(5)]  # Limits the value to a maximum of 100)
    )
    review_text = models.TextField()

    def __str__(self):
        return f"Testimonial: {self.review_text} 5-Star Rating: {self.star_rating}"
