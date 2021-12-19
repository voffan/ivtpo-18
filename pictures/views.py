from django.shortcuts import render
from django.http import HttpResponse
from pictures.models import Picture
from pictures.models import Genre
from pictures.models import Employee


# Create your views here.


def index(request):
    return render(request, "index.html", {'pictures': Picture.objects.all()})


def employee_list(request):
    return render(request, "employee.html", {'employees': Employee.objects.all()})


def index2(request):
    return render(request, "index2.html", {'pictures': Picture.objects.all()})


def genre_search(request):
    return render(request, "genre_list.html", {'genre': Genre.objects.all()})


