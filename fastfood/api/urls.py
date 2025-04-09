from django.urls import path
from .views import CategoryListCreate, FoodListCreate, OrderListCreate
from .views import FastFoodListCreateView, FastFoodDetailView

urlpatterns = [
    path('categories/', CategoryListCreate.as_view(), name='category-list'),
    path('foods/', FoodListCreate.as_view(), name='food-list'),
    path('orders/', OrderListCreate.as_view(), name='order-list'),
    path('fastfood/', FastFoodListCreateView.as_view(), name='fastfood-list'),
    path('fastfood/<int:pk>/', FastFoodDetailView.as_view(), name='fastfood-detail'),
]

