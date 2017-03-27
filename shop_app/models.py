from django.db import models
import datetime


class Product(models.Model):

    name = models.CharField(
        verbose_name='Product',
        max_length=32,
        null=False
    )

    price = models.DecimalField(
        verbose_name='price',
        null=False,
        decimal_places=2,
        max_digits=10
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Order(models.Model):

    email = models.EmailField(
        verbose_name='Email',
        null=False
    )

    sum = models.DecimalField(
        verbose_name='Sum',
        decimal_places=2,
        max_digits=10,
        null=False
    )

    date = models.DateTimeField(
        verbose_name='DateTime',
        auto_now_add=True
    )

    def __str__(self):
        return '# {0} - {1}'.format(self.id, self.email)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'