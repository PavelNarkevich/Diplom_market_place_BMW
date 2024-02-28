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

from apps.staff.models import (
    Order
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
            'engine_code',
            'model'
        ]


class CarElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarElement
        fields = '__all__'


class ComponentSerializer(serializers.ModelSerializer):
    element = serializers.SlugRelatedField(
        slug_field='name',
        queryset=CarElement.objects.all()
    )

    class Meta:
        model = Component
        fields = '__all__'


class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = [
            'id'
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


class AddBasketSerializer(serializers.ModelSerializer):
    items = serializers.SlugRelatedField(
        slug_field='id',
        queryset=Details.object.all(),
        read_only=False
    )

    class Meta:
        model = Basket
        fields = [
            'id',
            'quantity',
            'items',
            'price',
            'shopper'
        ]


class FullInfoDetailsSerializer(serializers.ModelSerializer):
    car = CarSerializer(many=True, read_only=True),
    component = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Component.objects.all()
    )

    class Meta:
        model = Details
        fields = '__all__'


class AddOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'shopper',
            'basket'
        ]


class DetailsForBaskerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = [
            'id',
            'name',
            'brand',
            'number',
            'price'
        ]


class UpdateBasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = [
            'id',
            'quantity',
            'price',
        ]


class BasketSerializer(serializers.ModelSerializer):
    items = DetailsForBaskerSerializer(read_only=True)

    class Meta:
        model = Basket
        fields = [
            'id',
            'quantity',
            'items',
            'price',
        ]


class GetUserOrderSerializer(serializers.ModelSerializer):
    basket = BasketSerializer(many=True, read_only=True)
    status = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = Order
        fields = [
            'id',
            'created_at',
            'updated_at',
            'basket',
            'status',
        ]
