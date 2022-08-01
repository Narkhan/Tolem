from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from api.services import get_distance

from api.models.restaurant import (
    Restaurant,
    Menu,
    FoodItem,
    Category,
    Order,
    OrderItem
)

from api.pagination import DefaultTolemPagination

from api.serializers import (
    RestaurantSerializer,
    MenuSerializer,
    FoodItemSerializer,
    CategorySerializer,
    OrderItemSerializer,
    OrderSerializer,
    RestaurantDistanceSerializer
)


class RestaurantViewSet(viewsets.mixins.ListModelMixin,
                        viewsets.mixins.RetrieveModelMixin,
                        viewsets.mixins.CreateModelMixin,
                        viewsets.mixins.DestroyModelMixin,
                        viewsets.mixins.UpdateModelMixin,
                        viewsets.GenericViewSet):
    pagination_class = DefaultTolemPagination

    def get_queryset(self):
        return Restaurant.objects.all()

    def get_serializer_class(self):
        return RestaurantSerializer

    @extend_schema(request=RestaurantDistanceSerializer)
    @action(detail=True, methods=['post'])
    def get_distance(self, request, pk):
        restaurant = self.get_object()
        latitude = request.data.get('latitude')
        longitude = request.data.get('longitude')

        return Response(get_distance(
            latitude,
            longitude,
            restaurant.latitude,
            restaurant.longitude,
        ))


class MenuViewSet(viewsets.mixins.ListModelMixin,
                  viewsets.mixins.RetrieveModelMixin,
                  viewsets.mixins.CreateModelMixin,
                  viewsets.mixins.DestroyModelMixin,
                  viewsets.mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    pagination_class = DefaultTolemPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('restaurant',)

    def get_queryset(self):
        return Menu.objects.all()

    def get_serializer_class(self):
        return MenuSerializer


class FoodItemViewSet(viewsets.mixins.ListModelMixin,
                      viewsets.mixins.RetrieveModelMixin,
                      viewsets.mixins.CreateModelMixin,
                      viewsets.mixins.DestroyModelMixin,
                      viewsets.mixins.UpdateModelMixin,
                      viewsets.GenericViewSet):
    pagination_class = DefaultTolemPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('category', 'is_active',)

    def get_queryset(self):
        return FoodItem.objects.all()

    def get_serializer_class(self):
        return FoodItemSerializer


class CategoryViewSet(viewsets.mixins.ListModelMixin,
                      viewsets.mixins.RetrieveModelMixin,
                      viewsets.mixins.CreateModelMixin,
                      viewsets.mixins.DestroyModelMixin,
                      viewsets.mixins.UpdateModelMixin,
                      viewsets.GenericViewSet):
    pagination_class = DefaultTolemPagination

    def get_queryset(self):
        return Category.objects.all()

    def get_serializer_class(self):
        return CategorySerializer


class OrderViewSet(viewsets.mixins.ListModelMixin,
                   viewsets.mixins.RetrieveModelMixin,
                   viewsets.mixins.CreateModelMixin,
                   viewsets.mixins.DestroyModelMixin,
                   viewsets.mixins.UpdateModelMixin,
                   viewsets.GenericViewSet):
    pagination_class = DefaultTolemPagination

    def get_queryset(self):
        return Order.objects.all()

    def get_serializer_class(self):
        return OrderSerializer


class OrderItemViewSet(viewsets.mixins.ListModelMixin,
                       viewsets.mixins.RetrieveModelMixin,
                       viewsets.mixins.CreateModelMixin,
                       viewsets.mixins.DestroyModelMixin,
                       viewsets.mixins.UpdateModelMixin,
                       viewsets.GenericViewSet):
    pagination_class = DefaultTolemPagination

    def get_queryset(self):
        return OrderItem.objects.all()

    def get_serializer_class(self):
        return OrderItemSerializer

