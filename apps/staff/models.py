from django.contrib.auth.models import User
from django.db import models
from apps.catalog.models import Basket

order_status_choice = [
    ('P', 'Pending'),
    ('C', 'Confirmed'),
    ('D', 'Done'),
    ('R', 'Rejection')
]

chat_status_choice = [
    ('P', 'Pending'),
    ('T', 'Taken'),
    ('D', 'Done')
]


class Order(models.Model):
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
        choices=order_status_choice,
        default='P'
    )

    object = models.Manager()

    def __str__(self):
        return f'{self.phone}'

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Order'


class Massage(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return f'{self.user} - {self.content}'

    class Meta:
        verbose_name = 'Massage'
        verbose_name_plural = 'Massages'


class Chats(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    helper = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='helper'
    )
    massages = models.ManyToManyField(Massage)
    status = models.CharField(
        max_length=1,
        choices=order_status_choice,
        default='P'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return f'{self.user}, {self.status}'

    class Meta:
        verbose_name = 'Chat'
        verbose_name_plural = 'Chats'
