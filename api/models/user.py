from django.db import models
from django.contrib.auth.models import AbstractUser

from api.models.restaurant import Restaurant


class User(AbstractUser):
    phone = models.CharField(
        max_length=50,
        verbose_name='Phone'
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name='Is Staff',
        help_text='Is Staff'
    )

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username


class Manager(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='User manager',
        help_text='User manager'
    )
    # FIXME: need to change to foreign key
    company = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Manager'
        verbose_name_plural = 'Managers'

    def __str__(self):
        return self.user.username
