from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import OrderViewSet

router = DefaultRouter()


router.register('order', OrderViewSet, basename='order' )

urlpatterns = [
    path('', include(router.urls)),
]
