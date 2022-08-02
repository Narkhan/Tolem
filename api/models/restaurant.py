from django.db import models
from django.conf import settings
from django.core.validators import (
    MaxValueValidator,
    MinValueValidator
)


class TimestampMixin(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created time'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Updated time'
    )


class Category(TimestampMixin):
    name = models.CharField(
        max_length=255,
        verbose_name='Food category',
        help_text='Food category'
    )

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Restaurant(TimestampMixin):
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
    latitude = models.FloatField(
        verbose_name='Latitude',
        help_text='Restaurant latitude'
    )
    longitude = models.FloatField(
        verbose_name='Longitude',
        help_text='Restaurant longitude'
    )

    class Meta:
        verbose_name = 'Restaurant'
        verbose_name_plural = 'Restaurants'

    def __str__(self):
        return self.name


class FoodItem(TimestampMixin):
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
    price = models.PositiveIntegerField(
        default=0,
        help_text='Price of food item'
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.DO_NOTHING,
        related_name='food_items',
        verbose_name='Food category',
        help_text='Food category'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Is active?',
        help_text='Is active?'
    )

    class Meta:
        verbose_name = 'Food item'
        verbose_name_plural = 'Food items'

    def __str__(self):
        return self.name


class Menu(TimestampMixin):
    restaurant = models.OneToOneField(
        Restaurant,
        on_delete=models.DO_NOTHING,
        verbose_name='Restaurant menu',
        help_text='Restaurant menu'
    )

    food_items = models.ManyToManyField(
        FoodItem,
        verbose_name='Food items',
        help_text='Food items'
    )

    def __str__(self):
        return f"Menu - {self.restaurant.name}"


class Review(TimestampMixin):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        verbose_name='User',
        help_text='User'
    )
    restaurant = models.OneToOneField(
        Restaurant,
        on_delete=models.DO_NOTHING,
        verbose_name='Restaurant review',
        help_text='Restaurant review'
    )
    description = models.CharField(
        max_length=255,
        verbose_name='Description',
        help_text='Review description'
    )
    rating = models.PositiveSmallIntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return f"Review - {self.restaurant.name}"


class Order(TimestampMixin):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        verbose_name='User that ordered',
        help_text='User that ordered'
    )
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.DO_NOTHING,
        verbose_name='Restaurant',
        help_text='Restaurant'
    )
    order_item = models.ManyToManyField(
        'OrderItem',
        related_name='order_items',
        verbose_name='Order items',
        help_text='Order items'
    )
    complete = models.BooleanField(
        default=False,
        verbose_name='Is complete?',
        help_text='Is complete?'
    )
    transaction_id = models.CharField(
        max_length=255,
        verbose_name='Transaction ID',
        help_text='Transaction ID'
    )
    is_paid = models.BooleanField(
        default=False,
        verbose_name='Is paid?',
        help_text='Is paid?'
    )
    received = models.BooleanField(
        default=False,
        verbose_name='Is received?',
        help_text='Is received?'
    )
    table_number = models.PositiveSmallIntegerField(
        verbose_name='Table number',
        help_text='Table number'
    )

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f"Order - {self.transaction_id}"


class OrderItem(TimestampMixin):
    order = models.ForeignKey(
        Order,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Order',
        help_text='Order'
    )
    food_item = models.ForeignKey(
        FoodItem,
        on_delete=models.DO_NOTHING,
        verbose_name='Food item',
        help_text='Food item'
    )
    quantity = models.PositiveSmallIntegerField(
        default=1,
        verbose_name='Quantity',
        help_text='Quantity'
    )

    class Meta:
        verbose_name = 'Order item'
        verbose_name_plural = 'Order items'

    def __str__(self):
        return f"Order item - {self.food_item.name} - {self.quantity}"

