from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'library/home.html')


def about(request):
    return render(request, 'library/about.html')
