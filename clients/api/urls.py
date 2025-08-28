from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ClientsViewSet

client_router = DefaultRouter()
client_router.register(r'clients', ClientsViewSet)
