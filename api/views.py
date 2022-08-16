from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from api.services import get_distance

from api.models import (
    User,
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
    RestaurantDistanceSerializer,
    RestaurantStatisticsSerializer,
    UserCreateSerializer,
    ObtainTokenSerializer,
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
        if self.action == 'statistics':
            return RestaurantStatisticsSerializer
        return RestaurantSerializer

    @extend_schema(request=RestaurantDistanceSerializer)
    @action(detail=True, methods=['post'])
    def distance(self, request, pk):
        restaurant = self.get_object()
        latitude = request.data.get('latitude')
        longitude = request.data.get('longitude')

        return Response({
            'distance': get_distance(
                latitude,
                longitude,
                restaurant.latitude,
                restaurant.longitude
            )
        })

    @action(detail=True, methods=['get'])
    def statistics(self, request, pk):
        restaurant = self.get_object()
        print(restaurant)
        serializer = self.get_serializer(restaurant)
        return Response(serializer.data)


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


class UserViewSet(viewsets.mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    pagination_class = DefaultTolemPagination

    def get_queryset(self):
        return User.objects.all()

    def get_serializer_class(self):
        if self.action == 'login':
            return ObtainTokenSerializer
        return UserCreateSerializer

    @action(detail=False, methods=['post'])
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

