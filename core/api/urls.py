from plans.api.urls import plan_router
from testimonials.api.urls import testimonial_router
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.registry.extend(plan_router.registry)
router.registry.extend(testimonial_router.registry)

urlpatterns = [
    path('', include(router.urls)),
]
