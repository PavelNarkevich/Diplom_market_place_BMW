from rest_framework import serializers

from apps.catalog.serializers import  BasketSerializer

from apps.staff.models import Order


class UpdateOrderSerializer(serializers.ModelSerializer):
    # status = serializers.CharField(source='get_status_display')

    class Meta:
        model = Order
        fields = [
            'id',
            'status'
        ]


class AddStaffOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['phone']


class GetOrderSerializer(serializers.ModelSerializer):
    basket = BasketSerializer(many=True, read_only=True)
    status = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = Order
        fields = [
            'id',
            'shopper',
            'phone',
            'created_at',
            'updated_at',
            'basket',
            'status',
        ]
