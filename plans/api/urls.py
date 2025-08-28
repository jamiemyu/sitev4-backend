from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PlansViewSet

plan_router = DefaultRouter()
plan_router.register(r'plans', PlansViewSet)
