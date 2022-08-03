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
            'address',
            'latitude',
            'longitude',
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
            'user',
            'order_item',
            'complete',
            'transaction_id',
            'is_paid',
            'received'
        )


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = (
            'id',
            'food_item',
            'quantity'
        )


class RestaurantDistanceSerializer(serializers.Serializer):
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()


class RestaurantStatisticsSerializer(serializers.ModelSerializer):
    food_item_number = serializers.SerializerMethodField()
    order_number = serializers.SerializerMethodField()
    order_item_number = serializers.SerializerMethodField()

    class Meta:
        model = Restaurant
        fields = (
            'id',
            'name',
            'food_item_number',
            'order_number',
            'order_item_number',
        )

    def get_order_number(self, obj) -> int:
        return obj.order_set.count()

    def get_food_item_number(self, obj) -> int:
        return obj.menu.food_items.count()

    def get_order_item_number(self, obj) -> int:
        return sum([order.order_item.count() for order in obj.order_set.all()])
