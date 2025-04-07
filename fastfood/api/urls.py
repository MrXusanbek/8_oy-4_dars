from django.urls import path
from .views import CategoryListCreate, FoodListCreate, OrderListCreate

urlpatterns = [
    path('categories/', CategoryListCreate.as_view(), name='category-list'),
    path('foods/', FoodListCreate.as_view(), name='food-list'),
    path('orders/', OrderListCreate.as_view(), name='order-list'),
]
