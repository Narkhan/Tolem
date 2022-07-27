from rest_framework import serializers

from api.models.restaurant import (
    Restaurant,
    Menu,
    FoodItem,
    Category,
    Order,
    OrderItem
)


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = (
            'id',
            'name',
            'address'
        )


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = (
            'id',
            'restaurant',
            'food_items'
        )


class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = (
            'id',
            'name',
            'description',
            'price',
            'category',
            'is_active'
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name'
        )


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'id',
            'restaurant',
            'food_items'
        )


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = (
            'id',
            'order',
            'food_item',
            'quantity'
        )
