from rest_framework import serializers
from .models import Category, MenuItem


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "restaurant"]

  

class MenuItemSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=False)
    restaurant = serializers.StringRelatedField(many=False)
    class Meta:
        model = MenuItem
        fields = '__all__'