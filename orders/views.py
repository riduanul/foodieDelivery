from django.shortcuts import render
from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# Create your views here.


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # permission_classes = [IsAuthenticated]

    #get your restaurant's orders
    def get_queryset(self):
        user = self.request.user
        if user.role == 'owner' or user.role == 'employee':
            return Order.objects.filter(restaurant = user.restaurant)
        else:
            return Order.objects.filter(user=user)
    
    # if owner or employee try to order
    def perform_create(self, serializer):
        user = self.request.user
        if user.restaurant is None and user.role != 'customer':
            return Response({"Error": "Employee or owner must be associate with a restaurant"}, status = 400)
        serializer.save(user=user, restaurant=user.restaurant)

    #get all orders by the current restaurant
    def by_restaurant(self, request):
        user = request.user

        if user.role != 'owner' or user.role != 'employee':
            return Response({"Error": "Only owner or employee can view this"}, status = 400)
        
        orders = Order.objects.filter(restaurant=user.restaurant)
        serializer = self.get_serializer(orders, many=True)
        return Response(serializer.data)




