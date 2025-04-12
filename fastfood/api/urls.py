from django.urls import path
from .views import CategoryListCreate, FoodListCreate, OrderListCreate
from .views import FastFoodListCreateView, FastFoodDetailView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.views.generic import TemplateView

urlpatterns = [
    path('categories/', CategoryListCreate.as_view(), name='category-list'),
    path('foods/', FoodListCreate.as_view(), name='food-list'),
    path('orders/', OrderListCreate.as_view(), name='order-list'),
    path('fastfood/', FastFoodListCreateView.as_view(), name='fastfood-list'),
    path('fastfood/<int:pk>/', FastFoodDetailView.as_view(), name='fastfood-detail'),
    path('', TemplateView.as_view(template_name='index.html')),
]

schema_view = get_schema_view(
   openapi.Info(
      title="FastFood API",
      default_version='v1',
      description="FastFood loyihasi uchun API hujjati",
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

