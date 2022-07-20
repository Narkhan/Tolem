from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from api.models.restaurant import Restaurant, Menu
from api.serializers import RestaurantSerializer, MenuSerializer


class RestaurantViewSet(mixins.ListModelMixin,
                        GenericViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class MenuViewSet(mixins.ListModelMixin,
                  GenericViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('restaurant',)