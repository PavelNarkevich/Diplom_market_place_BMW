from django.contrib import admin

from apps.staff.models import (
    Order
)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'shopper',
        'phone'
    )
