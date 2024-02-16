from django.urls import path
from apps.staff.views import (
    UpdateStatusOrdersGenericView,
    AddOrdersGenericView,
    GetOrderGenericView
)

urlpatterns = [
    path('orders/<int:id_order>/', UpdateStatusOrdersGenericView.as_view()),
    path('orders/', GetOrderGenericView.as_view()),
    path('orders/add/', AddOrdersGenericView.as_view()),
]
