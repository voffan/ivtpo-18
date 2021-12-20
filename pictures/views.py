from django.shortcuts import render
from django.http import HttpResponse

from pictures.models import Picture, Expo
from pictures.models import Picture, Employee, Artist

from pictures.models import Picture, Employee, Artist, Country



# Create your views here.


def index(request):
    return render(request, "index.html", {'pictures': Picture.objects.all()})


def authorization(request):
    return render(request, "authorization.html", {'pictures': Picture.objects.all()})


def artist_list(request):
    return render(request, "artist_list.html", {'artists': Artist.objects.all()})

def employee_list(request):
    return render(request, "employee.html", {'employees': Employee.objects.all()})


def listexpo(request):
    return render(request, "ListExpo.html", {'expo': Expo.objects.all()})

def countrySearch(request):
    return render(request, "country.html", {'countries': Country.objects.all()})


