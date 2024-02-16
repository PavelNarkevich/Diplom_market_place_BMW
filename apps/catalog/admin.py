from django.contrib import admin

from apps.catalog.models import (
    Transmission,
    EngineType,
    BodyType,
    Series,
    Cars,
    Country,
    Component,
    CarElement,
    Details,
    Basket,
)


@admin.register(Transmission)
class TransmissionAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(EngineType)
class EngineTypeAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(BodyType)
class BodyTypeAdmin(admin.ModelAdmin):
    list_display = ["body"]


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ['number']


@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    list_display = ['series', 'body', 'engine_type']


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(CarElement)
class CarElementAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Details)
class DetailAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'number',
        'quantity',
        'price'
    ]


@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ['quantity', 'shopper']

