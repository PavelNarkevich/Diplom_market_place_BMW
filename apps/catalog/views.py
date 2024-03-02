from rest_framework import status
from rest_framework.permissions import (
    DjangoModelPermissions,
    AllowAny,
    IsAuthenticated
)

from rest_framework.response import Response

from apps.catalog.parsing import Parsing

from apps.catalog.models import (
    Cars,
    CarElement,
    Component,
    Details,
    Basket,
)

from apps.catalog.serializers import (
    CatalogCarSerializer,
    TypeCarSerializer,
    FullInfoCarSerializer,
    CarElementSerializer,
    ComponentSerializer,
    BasketSerializer,
    FullInfoDetailsSerializer,
    AddOrderSerializer,
    AddBasketSerializer,
    GetUserOrderSerializer,
    UpdateBasketSerializer,
    CreateCarSerializer,
    CreateComponentSerializer,
    CreateDetailsSerializer,
)

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveAPIView,
    get_object_or_404,
    ListCreateAPIView,
)

from apps.staff.models import Order


class GetCatalogCarsGenericView(ListAPIView):
    serializer_class = CatalogCarSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Cars.objects.distinct('body')


class GetChoiceTypeCarGenericView(ListAPIView):
    serializer_class = TypeCarSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Cars.objects.filter(body=self.kwargs['body'])


class CreateCarsGenericView(ListCreateAPIView):
    serializer_class = CreateCarSerializer
    permission_classes = [DjangoModelPermissions]

    def get_queryset(self):
        return Cars.objects.all()

    def get(self, request, *args, **kwargs):
        instance = self.get_queryset()
        serializer = self.get_serializer(instance=instance, many=True)

        if instance:
            return Response(
                status=status.HTTP_200_OK,
                data=serializer.data
            )

        return Response(
            status=status.HTTP_204_NO_CONTENT,
            data=[]
        )

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return self.get(request, *args, **kwargs)

        return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data=[]
        )


class GetCarGenericView(ListAPIView):
    serializer_class = FullInfoCarSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Cars.objects.all()

    def get_object(self):
        data = {
            'car': Cars.objects.filter(id=self.kwargs['car_id']),
            'element': CarElement.objects.all()
        }
        return data

    def get(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance['car']:
            serializer_car = FullInfoCarSerializer(instance=instance.get('car'), many=True)
            serializer_element = CarElementSerializer(instance=instance.get('element'), many=True)

            data = {
                'car': serializer_car.data,
                'element': serializer_element.data
            }

            return Response(
                status=status.HTTP_200_OK,
                data=data
            )

        return Response(
            status=status.HTTP_204_NO_CONTENT,
            data=[]
        )


class UpdateDeleteCarsGenericView(RetrieveUpdateDestroyAPIView):
    serializer_class = CreateCarSerializer
    permission_classes = [DjangoModelPermissions]

    def get_queryset(self):
        return Cars.objects.all()

    def get_object(self):
        return get_object_or_404(Cars, id=self.kwargs['car_id'])

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance=instance)

        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )

    def put(self, request, *args, **kwargs):
        instance = get_object_or_404(Cars, id=self.kwargs['car_id'])
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

    def patch(self, request, *args, **kwargs):
        instance = get_object_or_404(Cars, id=self.kwargs['car_id'])
        serializer = self.serializer_class(instance=instance, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                status=status.HTTP_200_OK,
                data=serializer.data
            )

        return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data=serializer.errors
        )

    def delete(self, request, *args, **kwargs):
        instance = get_object_or_404(Cars, id=self.kwargs['car_id'])
        instance.delete()

        return Response(
            status=status.HTTP_200_OK,
            data=[]
        )


class GetComponentGenericView(ListAPIView):
    serializer_class = ComponentSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Component.objects.filter(element=self.kwargs['elem_id'], car=self.kwargs['car_id'])

    def get(self, request, *args, **kwargs):
        data = self.get_queryset()

        if data:
            serializer = self.serializer_class(instance=data, many=True)
            return Response(
                status=status.HTTP_200_OK,
                data=serializer.data
            )

        return Response(
            status=status.HTTP_204_NO_CONTENT,
            data=[]
        )


class GetDetailsGenericView(ListAPIView):
    serializer_class = FullInfoDetailsSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Details.object.filter(
            component=self.kwargs['component_id'],
            car=self.kwargs['car_id']
        )

    def get(self, request, *args, **kwargs):
        data = self.get_queryset()

        if data:
            serializer = self.serializer_class(instance=data, many=True)

            return Response(
                status=status.HTTP_200_OK,
                data=serializer.data
            )

        return Response(
            status=status.HTTP_204_NO_CONTENT,
            data=[]
        )



class GetBasketGenericView(ListAPIView):
    serializer_class = BasketSerializer
    permission_classes = [DjangoModelPermissions]

    def get_queryset(self):
        return Basket.object.filter(shopper=self.request.user.id, status='P')

    def get(self, request, *args, **kwargs):
        instance = self.get_queryset()

        if instance:
            serializer = self.serializer_class(instance=instance, many=True)

            return Response(
                status=status.HTTP_200_OK,
                data=serializer.data
            )

        return Response(
            status=status.HTTP_204_NO_CONTENT,
            data=[]
        )


class AddBasketGenericView(CreateAPIView):
    serializer_class = AddBasketSerializer
    permission_classes = [DjangoModelPermissions]

    def get_queryset(self):
        return Basket.object.all()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(
                status=status.HTTP_201_CREATED,
                data=serializer.data
            )

        return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data=serializer.errors
        )


class UpdateDeletedBasketGenericView(RetrieveUpdateDestroyAPIView):
    serializer_class = UpdateBasketSerializer
    permission_classes = [DjangoModelPermissions]

    def get_queryset(self):
        return Basket.object.all()

    def get_object(self):
        return get_object_or_404(
            Basket,
            items=self.kwargs['id_detail'],
            shopper=self.request.user,
            status='P'
        )

    def put(self, request, *args, **kwargs):
        instance = get_object_or_404(
            Basket,
            items=self.kwargs['id_detail'],
            shopper=self.request.user,
            status='P'
        )

        serializer = self.serializer_class(instance=instance, data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(
                status=status.HTTP_205_RESET_CONTENT,
                data=serializer.data
            )

        return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data=serializer.errors
        )

    def delete(self, request, *args, **kwargs):
        instance = get_object_or_404(
            Basket,
            items=self.kwargs['id_detail'],
            shopper=self.request.user,
            status='P'
        )

        instance.delete()
        return Response(
            status=status.HTTP_200_OK,
            data=[]
        )


class UpdateDeletedCarElementGenericView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarElementSerializer
    permission_classes = [DjangoModelPermissions]

    def get_queryset(self):
        return CarElement.objects.all()

    def get(self, request, *args, **kwargs):
        instance = get_object_or_404(CarElement, id=self.kwargs.get('elem_id'))
        serializer = self.serializer_class(instance=instance)

        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )

    def put(self, request, *args, **kwargs):
        instance = get_object_or_404(CarElement, id=self.kwargs.get('elem_id'))

        serializer = self.serializer_class(
            instance=instance,
            data=request.data
        )

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(
                status=status.HTTP_205_RESET_CONTENT,
                data=serializer.data
            )

        return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data=serializer.errors
        )

    def delete(self, request, *args, **kwargs):
        instance = get_object_or_404(CarElement, id=self.kwargs.get('elem_id'))
        instance.delete()

        return Response(
            status=status.HTTP_200_OK,
            data=[]
        )


class CreateCarElementGenericView(ListCreateAPIView):
    serializer_class = CarElementSerializer
    permission_classes = [DjangoModelPermissions]

    def get_queryset(self):
        return CarElement.objects.all()

    def get(self, request, *args, **kwargs):
        instance = self.get_queryset()

        serializer = self.serializer_class(instance=instance, many=True)

        if instance:
            return Response(
                status=status.HTTP_200_OK,
                data=serializer.data
            )

        return Response(
            status=status.HTTP_204_NO_CONTENT,
            data=[]
        )

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return self.get(request, *args, **kwargs)

        return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data=serializer.errors
        )


class CreateCarComponentGenericView(ListCreateAPIView):
    serializer_class = ComponentSerializer
    permission_classes = [DjangoModelPermissions]

    def get_queryset(self):
        return Component.objects.all()

    def get(self, request, *args, **kwargs):
        instance = self.get_queryset()
        serializer = self.serializer_class(instance=instance, many=True)

        if instance:
            return Response(
                status=status.HTTP_200_OK,
                data=serializer.data
            )

        return Response(
            status=status.HTTP_204_NO_CONTENT,
            data=[]
        )

    def post(self, request, *args, **kwargs):
        serializer = CreateComponentSerializer(data=request.data)

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


class UpdateCarComponentGenericView(RetrieveUpdateDestroyAPIView):
    serializer_class = CreateComponentSerializer
    permission_classes = [DjangoModelPermissions]

    def get_queryset(self):
        return Component.objects.all()

    def get_object(self):
        return Component.objects.filter(id=self.kwargs['id_component']).first()

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance=instance)

        if instance:
            return Response(
                status=status.HTTP_200_OK,
                data=serializer.data
            )

        return Response(
            status=status.HTTP_204_NO_CONTENT,
            data=[]
        )

    def put(self, request, *args, **kwargs):
        instance = get_object_or_404(Component, id=self.kwargs['id_component'])
        serializer = self.serializer_class(
            instance=instance,
            data=request.data
        )

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

    def delete(self, request, *args, **kwargs):
        instance = get_object_or_404(Component, id=self.kwargs['id_component'])
        instance.delete()

        return Response(
            status=status.HTTP_200_OK,
            data=[]
        )


class CreateDetailsGenericView(ListCreateAPIView):
    serializer_class = FullInfoDetailsSerializer
    permission_classes = [DjangoModelPermissions]

    def get_queryset(self):
        return Details.object.all()

    def get(self, request, *args, **kwargs):
        instance = self.get_queryset()
        serializer = self.serializer_class(instance=instance, many=True)

        if instance:
            return Response(
                status=status.HTTP_200_OK,
                data=serializer.data
            )

        return Response(
            status=status.HTTP_204_NO_CONTENT,
            data=[]
        )

    def post(self, request, *args, **kwargs):
        serializer = CreateDetailsSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(
                status=status.HTTP_201_CREATED,
                data=serializer.data
            )

        return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data=serializer.errors
        )


class UpdateDetailsGenericView(RetrieveUpdateDestroyAPIView):
    serializer_class = CreateDetailsSerializer
    permission_classes = [DjangoModelPermissions]

    def get_queryset(self):
        return Details.object.all()

    def get_object(self):
        return Details.object.filter(id=self.kwargs['id_detail']).first()

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance=instance)

        if instance:
            return Response(
                status=status.HTTP_200_OK,
                data=serializer.data
            )

        return Response(
            status=status.HTTP_404_NOT_FOUND,
            data=[]
        )

    def put(self, request, *args, **kwargs):
        instance = get_object_or_404(Details, id=self.kwargs['id_detail'])
        serializer = self.serializer_class(
            instance=instance,
            data=request.data
        )

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

    def delete(self, request, *args, **kwargs):
        instance = get_object_or_404(Details, id=self.kwargs['id_detail'])
        instance.delete()

        return Response(
            status=status.HTTP_200_OK,
            data=[]
        )


class CreateOrderGenericView(CreateAPIView):
    serializer_class = AddOrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.object.all()

    @staticmethod
    def deleted_basket_user(user):
        data = Basket.object.filter(shopper=user).all()

        for elem in data:
            elem.status = 'O'
            elem.save()

        return True

    def prepare_data(self):
        data = {
            **self.request.data,
            "phone": self.request.user.phone,
        }

        self.serializer_class.Meta.fields.append('phone')

        return data

    def post(self, request, *args, **kwargs):
        data = self.prepare_data()
        serializer = self.serializer_class(data=data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            self.deleted_basket_user(user=self.request.user.id)
            self.serializer_class.Meta.fields.remove('phone')

            return Response(
                status=status.HTTP_201_CREATED,
                data=serializer.data
            )

        self.serializer_class.Meta.fields.remove('phone')

        return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data=serializer.errors
        )


class GetCarByVinCodeGenericView(RetrieveAPIView):
    serializer_class = FullInfoCarSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Cars.objects.all()

    def get_object(self, *args, **kwargs):
        data = Parsing().get_car(vin_code=self.kwargs['vin_code'])
        if data:
            car = Cars.objects.filter(
                body=data.get('body'),
                body_type__body=data.get('body_type'),
                model=data.get('model'),
                engine_code=data.get('engine_code')
            ).first()

            return car

        return None

    def get(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance:
            serializer = self.get_serializer(instance=instance)

            return Response(
                status=status.HTTP_200_OK,
                data=serializer.data
            )

        return Response(
            status=status.HTTP_204_NO_CONTENT,
            data=[]
        )


class GetUserOrdersGenericView(ListAPIView):
    serializer_class = GetUserOrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.object.filter(shopper=self.request.user).all()


    def get(self, request, *args, **kwargs):
        instance = self.get_queryset()

        if instance:
            serializer = self.serializer_class(instance=instance, many=True)

            return Response(
                status=status.HTTP_200_OK,
                data=serializer.data
            )

        return Response(
            status=status.HTTP_204_NO_CONTENT,
            data=[]
        )
