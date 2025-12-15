from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='hote.home'),
    # path('', views.home, name='home'),
    path('authorized', views.AuthorizedView.as_view(), name='hote.authorized'),
    path('login', views.LoginInterfaceView.as_view(), name="hote.login"),
    path('logout', views.LogoutInterfaceView.as_view(), name="hote.logout"),
]

