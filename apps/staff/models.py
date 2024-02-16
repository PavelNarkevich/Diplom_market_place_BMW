from django.contrib.auth.models import User
from django.db import models
from apps.catalog.models import Basket


class Order(models.Model):
    status_choice = [
        ('P', 'Pending'),
        ('C', 'Confirmed'),
        ('D', 'Done'),
        ('R', 'Rejection')
    ]
    shopper = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    phone = models.CharField(
        max_length=40,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(
        null=True,
        blank=True,
    )
    basket = models.ManyToManyField(
        Basket
    )
    status = models.CharField(
        max_length=1,
        choices=status_choice,
        default='P'
    )

    object = models.Manager()

    def __str__(self):
        return f'{self.phone}'

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Order'
