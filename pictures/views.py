from django.shortcuts import render
from django.http import HttpResponse
from pictures.models import Picture, Employee, Country


# Create your views here.


def index(request):
    return render(request, "index.html", {'pictures': Picture.objects.all()})


def authorization(request):
    return render(request, "authorization.html", {'pictures': Picture.objects.all()})


def employee_list(request):
    return render(request, "employee.html", {'employees': Employee.objects.all()})


def index2(request):
    return render(request, "index2.html", {'pictures': Picture.objects.all()})

def countrySearch(request):
    return render(request, "country.html", {'countries': Country.objects.all()})

