from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Restaurant(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Name',
        help_text='Restaurant name'
    )
    address = models.CharField(
        max_length=255,
        verbose_name='Address',
        help_text='Restaurant address'
    )

    class Meta:
        verbose_name = 'Restaurant'
        verbose_name_plural = 'Restaurants'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Food category',
        help_text='Food category'
    )


class FoodItem(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Name',
        help_text='Food name'
    )
    description = models.CharField(
        max_length=255,
        verbose_name='Name',
        help_text='Food name'
    )
    price = models.FloatField(
        default=0,
        help_text='Price of food item'
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Menu(models.Model):
    restaurant = models.OneToOneField(
        Restaurant,
        on_delete=models.CASCADE,
        verbose_name='Restaurant menu',
        help_text='Restaurant menu'
    )

    food_items = models.ManyToManyField(FoodItem)


class Review(models.Model):
    restaurant = models.OneToOneField(
        Restaurant,
        on_delete=models.CASCADE,
        verbose_name='Restaurant review',
        help_text='Restaurant review'
    )
    description = models.CharField(
        max_length=255,
        verbose_name='description',
        help_text='Review description'
    )
    rating = models.PositiveSmallIntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
