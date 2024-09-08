from django.shortcuts import render
from rest_framework import viewsets
from .models import Category, MenuItem
from .serializers import CategorySerializer, MenuItemSerializer
from rest_framework.permissions import IsAuthenticated
from user.permissions import IsOwnerOrEmployee
# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes =[IsAuthenticated, IsOwnerOrEmployee]

    # def get_queryset(self):
    #     user = self.request.user
    #     # For owners and employees, return all categories of their restaurant
    #     if user.role in ['owner', 'employee']:
    #         return Category.objects.filter(restaurant=user.restaurant)
    #     # For customers, return only categories available for ordering
    #     return Category.objects.filter()

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    # permission_classes =[IsAuthenticated, IsOwnerOrEmployee]

    # def get_queryset(self):
    #     user = self.request.user
    #     # For owners and employees, return all menu items of their restaurant
    #     if user.role in ['owner', 'employee']:
    #         return MenuItem.objects.filter(restaurant=user.restaurant)
    #     # For customers, return only available menu items
    #     return MenuItem.objects.filter()
