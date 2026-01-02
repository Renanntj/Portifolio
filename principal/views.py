from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.

def home(requests):
    return render(requests, 'portifolio/pages/principal.html')
