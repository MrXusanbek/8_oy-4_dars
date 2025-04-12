from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Category, FastFood, Order
from .serializers import CategorySerializer, FastFoodSerializer, OrderSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAdminOrReadOnly
from rest_framework.throttling import UserRateThrottle

def home(request):
    return HttpResponse("<h1>Welcome to the FastFood API</h1><p>Visit <a href='/api/'>API Endpoints</a></p>")


class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class FoodListCreate(generics.ListCreateAPIView):
    queryset = FastFood.objects.all()
    serializer_class = FastFoodSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class OrderListCreate(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class FastFoodListCreateView(generics.ListCreateAPIView):
    queryset = FastFood.objects.all()
    serializer_class = FastFoodSerializer
    permission_classes = [IsAdminOrReadOnly]

class FastFoodDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FastFood.objects.all()
    serializer_class = FastFoodSerializer
    permission_classes = [IsAdminOrReadOnly]


class CustomFastFoodThrottle(UserRateThrottle):
    rate = '3/minute'

class FastFoodListCreateView(generics.ListCreateAPIView):
    ...
    throttle_classes = [CustomFastFoodThrottle]

