from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ClientsViewSet

testimonial_router = DefaultRouter()
testimonial_router.register(r'clients', ClientsViewSet)
