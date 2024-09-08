from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()

router.register('register', views.RegisterViewSet, basename='register')
router.register('login', views.UserLoginViewSet, basename='loign')


urlpatterns = [
    path("", include(router.urls)),
]

