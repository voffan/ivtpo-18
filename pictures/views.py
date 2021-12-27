from django.shortcuts import render, redirect
from django.http import HttpResponse
from pictures.models import Picture
from .form import PictureForm
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

def employee_list(request):
    return render(request, "employee.html", {'employees': Employee.objects.all()})

def index(request):
    return render(request, "index.html", {'pictures': Picture.objects.all()})


def index2(request):
    return render(request, "index2.html", {'pictures': Picture.objects.all()})
