from django.shortcuts import render
from django.http import HttpResponse
from pictures.models import Picture, Expo

# Create your views here.


def index(request):
    return render(request, "index.html", {'pictures': Picture.objects.all()})


def employee_list(request):
    return render(request, "employee.html", {'employees': Employee.objects.all()})


def listexpo(request):
    return render(request, "ListExpo.html", {'expo': Expo.objects.all()})
