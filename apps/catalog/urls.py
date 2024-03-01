from django.urls import (
    path
)

from apps.catalog.views import (
    GetCatalogCarsGenericView,
    GetChoiceTypeCarGenericView,
    CreateCarsGenericView,
    GetCarGenericView,
    UpdateDeleteCarsGenericView,
    GetComponentGenericView,
    GetDetailsGenericView,
    TestGenericView,
    GetBasketGenericView,
    AddBasketGenericView,
    UpdateDeletedBasketGenericView,
    UpdateDeletedCarElementGenericView,
    CreateCarElementGenericView,
    CreateCarComponentGenericView,
    UpdateCarComponentGenericView,
    CreateDetailsGenericView,
    UpdateDetailsGenericView,
    CreateOrderGenericView,
    GetCarByVinCodeGenericView,
    GetUserOrdersGenericView,
)

urlpatterns = [
    path('', GetCatalogCarsGenericView.as_view()),
    path('bmw/<str:body>/', GetChoiceTypeCarGenericView.as_view()),
    path('create_cars/', CreateCarsGenericView.as_view()),
    path('create_cars/<int:car_id>/', UpdateDeleteCarsGenericView.as_view()),
    path('create_el/', CreateCarElementGenericView.as_view()),
    path('create_el/<int:elem_id>/', UpdateDeletedCarElementGenericView.as_view()),
    path('create_component/', CreateCarComponentGenericView.as_view()),
    path('create_component/<int:id_component>/', UpdateCarComponentGenericView.as_view()),
    path('create_detail/', CreateDetailsGenericView.as_view()),
    path('create_detail/<int:id_detail>/', UpdateDetailsGenericView.as_view()),
    path('bmw/<str:body>/<int:car_id>/', GetCarGenericView.as_view()),
    path('bmw/<str:body>/<int:car_id>/<int:elem_id>/', GetComponentGenericView.as_view()),
    path('bmw/<str:body>/<int:car_id>/<int:elem_id>/<int:component_id>/', GetDetailsGenericView.as_view()),
    path('bmw/<str:body>/<int:car_id>/<int:elem_id>/<int:component_id>/addcart/', AddBasketGenericView.as_view()),
    path('test/', TestGenericView.as_view()),
    path('cart/', GetBasketGenericView.as_view()),
    path('cart/<int:id_detail>/', UpdateDeletedBasketGenericView.as_view()),
    path('cart/add_order/', CreateOrderGenericView.as_view()),
    path('search/<str:vin_code>/', GetCarByVinCodeGenericView.as_view()),
    path('order/',  GetUserOrdersGenericView.as_view()),
]
