from django.urls import path
from . import views

urlpatterns = [
    path('lists', views.list),
    path('details/<int:pk>', views.detail),
]