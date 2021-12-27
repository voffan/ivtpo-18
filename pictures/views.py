from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from pictures.models import Picture, Expo
from pictures.models import Picture, Employee, Artist
from pictures.models import Picture, Employee, Artist, Country
from django.views.decorators.csrf import csrf_exempt
from pictures.authForm import AuthForm



# Create your views here.


def index(request):
    return render(request, "index.html", {'pictures': Picture.objects.all()})

@csrf_exempt
def authorization(request):
    if request.method == "POST":
        #add authorization code
        form = AuthForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['login'], password=form.cleaned_data['pwd'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # Redirect to a success page.
                    return redirect('pictures:index')
    else:
        form = AuthForm
    return render(request, "authorization.html", {'form': form})


def artist_list(request):
    return render(request, "artist_list.html", {'artists': Artist.objects.all()})

def employee_list(request):
    return render(request, "employee.html", {'employees': Employee.objects.all()})


def listexpo(request):
    return render(request, "ListExpo.html", {'expo': Expo.objects.all()})

def countrySearch(request):
    return render(request, "country.html", {'countries': Country.objects.all()})


