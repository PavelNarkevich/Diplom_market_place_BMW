from rest_framework import serializers
from apps.catalog.models import (
    Cars,
    BodyType,
    Country,
    EngineType,
    Series,
    Transmission,
    CarElement,
    Component,
    Details,
    Basket
)


class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = 'name'


class CatalogCarSerializer(serializers.ModelSerializer):
    series = serializers.SlugRelatedField(
        slug_field='number',
        queryset=Series.objects.all()
    )

    class Meta:
        model = Cars
        fields = ['id', 'series', 'body']


class BodyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyType
        fields = 'body'


class TypeCarSerializer(serializers.ModelSerializer):
    body_type = serializers.SlugRelatedField(
        slug_field='body',
        queryset=BodyType.objects.all()
    )

    class Meta:
        model = Cars
        fields = [
            'id',
            'engine_code',
            'body_type',
            'model'
        ]


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = '__all__'


class FullInfoCarSerializer(serializers.ModelSerializer):
    body_type = serializers.SlugRelatedField(
        slug_field='body',
        queryset=BodyType.objects.all()
    )
    series = serializers.SlugRelatedField(
        slug_field='number',
        queryset=Series.objects.all()
    )
    engine_type = serializers.SlugRelatedField(
        slug_field='name',
        queryset=EngineType.objects.all()
    )
    transmission = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Transmission.objects.all()
    )
    country = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Country.objects.all()
    )

    class Meta:
        model = Cars
        fields = [
            'id',
            'body_type',
            'series',
            'engine_type',
            'transmission',
            'country',
            'body',
            'engine_code'
        ]


class CarElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarElement
        fields = '__all__'


class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = '__all__'


class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = [
            'name',
            'number',
            'price',
            'quantity',
            'description',
            'photo',
        ]


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = '__all__'


class BasketSerializer(serializers.ModelSerializer):
    items = serializers.SlugRelatedField(
        slug_field=['name', 'number', 'brand'],
        queryset=Details.object.all()
    )

    class Meta:
        model = Basket
        fields = [
            'id',
            'quantity',
            'items',
            'price',
            'shopper',
        ]


