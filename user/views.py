from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.viewsets import ViewSet
from .models import CustomUser
from .serializers import RegisterSerializer, UserLoginSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout 
from rest_framework.decorators import api_view


class RegisterViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    http_method_names = ['post'] # Only post request will be done

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # creating token
        token, created = Token.objects.get_or_create(user=user)

        return Response({"message": "User successfully Registered", "token": token.key, "user": {"username": user.username, "role": user.role, "restaurant": user.restaurant.name if user.restaurant else None } }, status= status.HTTP_201_CREATED)
    
class UserLoginViewSet(ViewSet):
    def create(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(request, username=username, password=password)
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'token': token.key, 'user_id': user.id})
            else:
                return Response({'error': 'Invalid credentials'}, status=400)

        return Response(serializer.errors, status=400)



    

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'admin': request.build_absolute_uri('/admin/'),
        'user_api': request.build_absolute_uri('/api/user/'),
        'menu_api': request.build_absolute_uri('/api/menu/'),
        'orders_api': request.build_absolute_uri('/api/orders/')
    })