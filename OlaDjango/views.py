from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.



def olamundo(request):
    return HttpResponse('Ola Mundo')

