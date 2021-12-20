from django.shortcuts import render
from django.http import HttpResponse
from pictures.models import Picture, Employee


# Create your views here.


def index(request):
    return render(request, "index.html", {'pictures': Picture.objects.all()})


def authorization(request):
    if request.method == "POST":
        #add authorization code

        pass
    return render(request, "authorization.html")


def employee_list(request):
    return render(request, "employee.html", {'employees': Employee.objects.all()})


def index2(request):
    return render(request, "index2.html", {'pictures': Picture.objects.all()})

