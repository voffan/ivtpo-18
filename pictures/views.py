from django.shortcuts import render, redirect
from django.http import HttpResponse

from pictures.models import Expo, Genre

from pictures.models import Picture, Employee, Artist, Country

# Create your views here.


def piclist(request):
    error = ''
    if request.method == 'POST':
        form = PictureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/')
        else:
            error = 'Форма была неверной'
    form = PictureForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, "indexpl.html", data)

def authorization(request):
    return render(request, "authorization.html", {'pictures': Picture.objects.all()})


def artist_list(request):
    return render(request, "artist_list.html", {'artists': Artist.objects.all()})

def employee_list(request):
    return render(request, "employee.html", {'employees': Employee.objects.all()})

def index(request):
    return render(request, "index.html", {'pictures': Picture.objects.all()})


def listexpo(request):
    return render(request, "ListExpo.html", {'expo': Expo.objects.all()})


def country_list(request):
    return render(request, "country_list.html", {'countries': Country.objects.all()})

def genre_search(request):
    return render(request, "genre_list.html", {'genres': Genre.objects.all()})

def picture_detail(request, picture_id):

    return render(request, "picture_details.html", {'pictures': Picture.objects.all().filter(id = picture_id)})


