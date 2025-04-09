from rest_framework import serializers
from .models import Category, FastFood, Order

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class FastFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = FastFood
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
