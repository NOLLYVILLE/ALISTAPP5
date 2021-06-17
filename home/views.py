from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def travelapp(request):
    return HttpResponse('This is a special travelapp with the best travel company')