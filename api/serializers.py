from rest_framework import serializers

from api.models.restaurant import (
    Restaurant,
    Menu,
    FoodItem,
    Category,
    Order,
    OrderItem
)
from api.models.user import User
from rest_framework.authtoken.models import Token


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'password',
        )
        extra_kwargs = {
            'username': {'write_only': True},
            'password': {'write_only': True},
        }

    def validate_username(self, value):
        if not value:
            raise serializers.ValidationError('Username is required')
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError('User with that username already exists')
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )
        print(user)
        Token.objects.get_or_create(user=user)
        return user


class ObtainTokenSerializer(serializers.Serializer):
    token = serializers.CharField(
        read_only=True
    )
    username = serializers.CharField(
        write_only=True,
    )
    password = serializers.CharField(
        write_only=True
    )

    def validate(self, attrs):
        validated_data = super().validate(attrs)
        user = User.objects.filter(
            username=validated_data['username']
        ).first()
        if not user:
            raise serializers.ValidationError('User does not exists')
        is_valid_password = user.check_password(validated_data['password'])
        if not is_valid_password:
            raise serializers.ValidationError('Invalid password')
        token, _ = Token.objects.get_or_create(user=user)
        validated_data['token'] = token.key
        return validated_data


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
    cost = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = (
            'user',
            'order_item',
            'complete',
            'transaction_id',
            'is_paid',
            'received',
            'cost'
        )

    def get_cost(self, obj) -> int:
        return sum([item.quantity * item.food_item.price for item in obj.order_item.all()])


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
