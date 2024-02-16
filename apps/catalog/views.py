from rest_framework import status
from rest_framework.response import Response

from apps.catalog.models import (
    Cars,
    CarElement,
    Component,
    Details, Basket,
)

from apps.catalog.serializers import (
    CatalogCarSerializer,
    TypeCarSerializer,
    CarSerializer,
    FullInfoCarSerializer,
    CarElementSerializer,
    ComponentSerializer,
    DetailsSerializer,
    TestSerializer,
    BasketSerializer,
)

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveAPIView, UpdateAPIView,
)


class GetCatalogCarsGenericView(ListAPIView):
    serializer_class = CatalogCarSerializer

    def get_queryset(self):
        return Cars.objects.distinct('body')


class GetChoiceTypeCarGenericView(ListAPIView):
    serializer_class = TypeCarSerializer

    def get_queryset(self):
        return Cars.objects.filter(body=self.kwargs['body'])


class CreateCarsGenericView(CreateAPIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        return Cars.objects.all()


class GetCarGenericView(ListAPIView):

    def get_queryset(self):
        car = Cars.objects.filter(id=self.kwargs['car_id'])
        if car:
            return car

        return Response(
            status=status.HTTP_204_NO_CONTENT,
            data=[]
        )

    def get_object(self):
        data = {
            'car': Cars.objects.filter(id=self.kwargs['car_id']),
            'element': CarElement.objects.all()
        }
        return data

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
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


class UpdateDeleteCarsGenericView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        return Cars.objects.filter(id=self.kwargs['car_id'])

    def get_object(self):
        data = Cars.objects.filter(id=self.kwargs['car_id'])
        if data:
            return data

        return Response(
            status=status.HTTP_204_NO_CONTENT,
            data=[]
        )

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance=instance, many=True)

        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )


class GetComponentGenericView(ListAPIView):
    serializer_class = ComponentSerializer

    def get_queryset(self):
        return Component.objects.filter(element=self.kwargs['elem_id'])

    def get(self, request, *args, **kwargs):
        data = list(self.get_queryset())

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
    serializer_class = DetailsSerializer

    def get_queryset(self):
        return Details.object.filter(
            component=self.kwargs['component_id'],
            car=self.kwargs['car_id']
        )

    def get(self, request, *args, **kwargs):
        data = list(self.get_queryset())

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


class TestGenericView(RetrieveAPIView):
    serializer_class = TestSerializer

    def get_queryset(self):
        return Details.object.all()

    def get(self, request, *args, **kwargs):
        data = Details.object.filter(id=1).first()
        new_data = data.price
        print(new_data)

        serializer = self.serializer_class(instance=data)

        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )


class GetBasketGenericView(ListAPIView):
    serializer_class = BasketSerializer

    def get_queryset(self):
        return Basket.object.all()

    def get(self, request, *args, **kwargs):
        instance = list(self.get_queryset())

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
    serializer_class = BasketSerializer

    def get_queryset(self):
        return Basket.object.all()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
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
    serializer_class = BasketSerializer

    def get_queryset(self):
        return Basket.object.all()

    def get_object(self):
        return Basket.object.filter(
            shopper=self.request.user,
            items=self.kwargs['']
        )
