from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class EnrollmentStatus(models.TextChoices):
    EXPRESSED_INTEREST = "EXPRESSED_INTEREST", "Expressed Interest"
    ENROLLED = "ENROLLED", "Enrolled"
    RETIRED = "RETIRED", "Retired"


class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField(blank=True)
    enrollment_status = models.CharField(
        max_length=20,
        choices=EnrollmentStatus.choices,
        default=EnrollmentStatus.EXPRESSED_INTEREST,
    )

    def __str__(self):
        return f"Client: {self.first_name} {self.last_name}"
