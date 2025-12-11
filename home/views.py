from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    dataArray = {'date': datetime.now().strftime("%b %d, %Y %H:%M:%S")}
    return render(request, 'home/index.html', dataArray)

@login_required(login_url='/admin/')
def authorized(request):
    dataArray = {}
    return render(request, 'home/authorized.html', dataArray)
