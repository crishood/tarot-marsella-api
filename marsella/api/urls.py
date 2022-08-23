from django.urls import path
from .views import CardList, CardDetail

urlpatterns = [
    path('card/', CardList.as_view()),
    path('card/<int:pk>', CardDetail.as_view()),
]