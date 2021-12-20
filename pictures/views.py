from django.shortcuts import render
from django.http import HttpResponse
from pictures.models import Picture, Artist


# Create your views here.


def index(request):
    return render(request, "index.html", {'pictures': Picture.objects.all()})


def artist_list(request):
    return render(request, "artist_list.html", {'artists': Artist.objects.all()})
