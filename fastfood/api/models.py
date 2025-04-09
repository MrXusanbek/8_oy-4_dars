from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# class Food(models.Model):
#     name = models.CharField(max_length=200)
#     price = models.DecimalField(max_digits=6, decimal_places=2)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.name
from django.db import models

class FastFood(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name


class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    food = models.ManyToManyField(FastFood)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_name
