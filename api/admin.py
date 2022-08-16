from django.contrib import admin

# Register your models here.
from api.models import (
    User,
    Restaurant,
    Menu,
    FoodItem,
    Category,
    Order,
    OrderItem,
)

admin.site.register(Restaurant)
admin.site.register(Menu)
admin.site.register(FoodItem)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(User)

