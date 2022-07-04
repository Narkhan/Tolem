from django.db import models

from api.models.restaurant import Restaurant


class User(models.Model):
    username = models.CharField(
        max_length=50,
        verbose_name='Username',
        unique=True,
        help_text='Username for login'
    )
    password = models.CharField(
        max_length=50,
        verbose_name='Password',
        help_text='Password for login'
    )
    email = models.EmailField(
        max_length=254,
        verbose_name='Email',
        unique=True,
        help_text='Email for login'
    )
    first_name = models.CharField(
        max_length=50,
        verbose_name='First Name',
        help_text='First Name'
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name='Last Name',
        help_text='Last Name'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Is Active',
        help_text='Is Active'
    )
    is_admin = models.BooleanField(
        default=False,
        verbose_name='Is Admin',
        help_text='Is Admin'
    )
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
