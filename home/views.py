from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class HomeView(TemplateView):
    # pass the code
    template_name = "home/index.html"
    extra_content = {'currentDay': datetime.now().strftime("%b %d, %Y %H:%M:%S")}
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
