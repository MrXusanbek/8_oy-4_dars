from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Category, Food, Order
from .serializers import CategorySerializer, FoodSerializer, OrderSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

def home(request):
    return HttpResponse("<h1>Welcome to the FastFood API</h1><p>Visit <a href='/api/'>API Endpoints</a></p>")


class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class FoodListCreate(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class OrderListCreate(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]



