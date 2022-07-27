from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from api.models.restaurant import Restaurant, Menu
from api.serializers import RestaurantSerializer, MenuSerializer


class RestaurantViewSet(viewsets.mixins.ListModelMixin,
                        viewsets.GenericViewSet):

    def get_queryset(self):
        if self.action == 'list':
            return Restaurant.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return RestaurantSerializer


class MenuViewSet(viewsets.mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('restaurant',)

    def get_queryset(self):
        if self.action == 'list':
            return Menu.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return MenuSerializer
