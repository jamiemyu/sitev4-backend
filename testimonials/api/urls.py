from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TestimonialsViewSet

testimonial_router = DefaultRouter()
testimonial_router.register(r'testimonials', TestimonialsViewSet)
