from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.permissions import AllowAny, DjangoModelPermissions
from rest_framework.response import Response

from rest_framework.generics import (
    RetrieveUpdateAPIView,
    get_object_or_404,
    ListAPIView,
    CreateAPIView,
)

from apps.catalog.models import Basket
from apps.staff.models import Order
from apps.staff.serializers import (
    UpdateOrderSerializer,
    AddStaffOrderSerializer,
    GetOrderSerializer
)


class UpdateStatusOrdersGenericView(RetrieveUpdateAPIView):
    serializer_class = UpdateOrderSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Order.object.all()

    def get_object(self):
        return get_object_or_404(Order, id=self.kwargs['id_order'])

    def get(self, request, *args, **kwargs):
        instance = self.get_object()

        serializer = self.serializer_class(instance=instance, many=False)

        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )


    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance=instance, data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(
                status=status.HTTP_200_OK,
                data=serializer.data
            )

        return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data=serializer.errors
        )


class AddOrdersGenericView(CreateAPIView):
    serializer_class = AddStaffOrderSerializer
    permission_classes = [DjangoModelPermissions]

    def get_queryset(self):
        return Order.object.all()

    def search_user(self):
        user = User.objects.filter(phone=self.request.data.get('phone')).first()

        if user:
            return user.id

        return None

    @staticmethod
    def deleted_basket_user(user):
        data = Basket.object.filter(shopper=user).all()

        for elem in data:
            elem.status = 'O'
            elem.save()

        return True

    def get_basket(self):
        basket = Basket.object.filter(shopper=self.request.user.id, status='P').all()
        basket_id = [elem.id for elem in basket]
        return basket_id

    def prepare_data(self):
        data = {
            **self.request.data,
            'shopper': self.search_user(),
            'status': 'C',
            'basket': self.get_basket(),

        }

        self.serializer_class.Meta.fields.append('shopper')
        self.serializer_class.Meta.fields.append('status')
        self.serializer_class.Meta.fields.append('basket')
        return data

    def post(self, request, *args, **kwargs):
        data = self.prepare_data()
        serializer = self.get_serializer(data=data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            self.serializer_class.Meta.fields.remove('shopper')
            self.serializer_class.Meta.fields.remove('status')
            self.serializer_class.Meta.fields.remove('basket')

            self.deleted_basket_user(user=self.request.user.id)

            return Response(
                status=status.HTTP_201_CREATED,
                data=serializer.data
            )

        self.serializer_class.Meta.fields.remove('shopper')
        self.serializer_class.Meta.fields.remove('status')
        self.serializer_class.Meta.fields.remove('basket')

        return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data=serializer.errors
        )


class GetOrderGenericView(ListAPIView):
    serializer_class = GetOrderSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Order.object.all()

    def get(self, request, *args, **kwargs):
        instance = self.get_queryset()

        if instance:
            serializer = self.get_serializer(instance=instance, many=True)

            return Response(
                status=status.HTTP_200_OK,
                data=serializer.data
            )

        return Response(
            status=status.HTTP_204_NO_CONTENT,
            data=[]
        )
