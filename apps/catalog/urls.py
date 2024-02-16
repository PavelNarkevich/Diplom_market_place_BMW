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
)

urlpatterns = [
    path('', GetCatalogCarsGenericView.as_view()),
    path(' <str:body>', GetChoiceTypeCarGenericView.as_view()),
    path('create_cars/', CreateCarsGenericView.as_view()),
    path(' <str:body>/<int:car_id>/update_cars/', UpdateDeleteCarsGenericView.as_view()),
    path(' <str:body>/<int:car_id>', GetCarGenericView.as_view()),
    path(' <str:body>/<int:car_id>/<int:elem_id>', GetComponentGenericView.as_view()),
    path(' <str:body>/<int:car_id>/<int:elem_id>/<int:component_id>', GetDetailsGenericView.as_view()),
    path(' <str:body>/<int:car_id>/<int:elem_id>/<int:component_id>/addcart/', AddBasketGenericView.as_view()),
    path('test/', TestGenericView.as_view()),
    path('cart/', GetBasketGenericView.as_view())
]
