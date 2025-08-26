from posts.api.urls import post_router
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.registry.extend(post_router.registry)

urlpatterns = [
    path('', include(router.urls)),
]
