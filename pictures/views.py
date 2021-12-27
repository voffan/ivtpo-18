from django.shortcuts import render
from django.http import HttpResponse

from pictures.models import Expo, Genre

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


def country_list(request):
    return render(request, "country_list.html", {'countries': Country.objects.all()})

def genre_search(request):
    return render(request, "genre_list.html", {'genres': Genre.objects.all()})

def picture_detail(request, picture_id):

    return render(request, "picture_details.html", {'picture': Picture.objects.all().get(id = picture_id)})


