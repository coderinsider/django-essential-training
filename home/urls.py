from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view()),
    # path('', views.home, name='home'),
    path('authorized', views.AuthorizedView.as_view()),
]

