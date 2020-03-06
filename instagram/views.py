from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
from django.http  import HttpResponse,Http404
from django.shortcuts import render


# Create your views here.
def welcome(request):
    return render(request,'welcome.html')
