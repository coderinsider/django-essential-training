from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
# Create your views here.
class LoginInterfaceView(LoginView):
    template_name = "home/login.html"

class LogoutInterfaceView(LogoutView):
    template_name = "home/logout.html"
    http_method_names = 'get'

class HomeView(TemplateView):
    # pass the code
    template_name = "home/welcome.html"
    extra_context = {'currentDay': datetime.now().strftime("%b %d, %Y %H:%M:%S")}
# def home(request):
#     dataArray = {'date': datetime.now().strftime("%b %d, %Y %H:%M:%S")}
#     return render(request, 'home/index.html', dataArray)


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = "home/authorized.html"
    login_url = "/admin/"

# @login_required(login_url='/admin/')
# def authorized(request):
#     dataArray = {}
#     return render(request, 'home/authorized.html', dataArray)
