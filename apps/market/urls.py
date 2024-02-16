from django.urls import (
    path
)

from apps.market.views import (
    GetInfoCompanyGenericView,
    PutInfoCompanyGenericView,
    GetCreateSocialNetworkGenericView,
    GetCreateWorkTimeGenericView,
    UpdateDeleteWorkTimeGenericView,
    UpdateDeleteSocialNetworkGenericView,
    GetNewsGenericView,
    CreateNewsGenericView,
    UpdateDeleteNewsGenericView,
)

urlpatterns = [
    path('', GetInfoCompanyGenericView.as_view()),
    path('update/', PutInfoCompanyGenericView.as_view()),
    path('social_network/', GetCreateSocialNetworkGenericView.as_view()),
    path('work_time/', GetCreateWorkTimeGenericView.as_view()),
    path('work_time/<int:id>/', UpdateDeleteWorkTimeGenericView.as_view()),
    path('social_network/<int:id>/', UpdateDeleteSocialNetworkGenericView.as_view()),
    path('news/', GetNewsGenericView.as_view()),
    path('news/create/', CreateNewsGenericView.as_view()),
    path('news/<int:id_news>/', UpdateDeleteNewsGenericView.as_view()),
]
