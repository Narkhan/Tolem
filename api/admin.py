from django.contrib import admin

# Register your models here.
from api.models.restaurant import Restaurant, Menu, FoodItem, Category

admin.site.register(Restaurant)
admin.site.register(Menu)
admin.site.register(FoodItem)
admin.site.register(Category)