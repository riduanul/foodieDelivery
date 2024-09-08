from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CategoryViewSet, MenuItemViewSet

router = DefaultRouter()


router.register('category', CategoryViewSet, basename='category' )
router.register('menuItem', MenuItemViewSet, basename='menuItem' )

urlpatterns = [
    path('', include(router.urls)),
]
