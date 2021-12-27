from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from pictures.models import Picture, Expo
from pictures.models import Picture, Employee, Artist
from pictures.models import Picture, Employee, Artist, Country
from django.views.decorators.csrf import csrf_exempt



# Create your views here.


def index(request):
    return render(request, "index.html", {'pictures': Picture.objects.all()})

@csrf_exempt
def authorization(request):
    if request.method == "POST":
        #add authorization code
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to a success page.
                print("User is valid, active and authenticated")
            else:
                print("The password is valid, but the account has been disabled!")
                # Return a 'disabled account' error message

        else:
            print("aboba")
        # Return an 'invalid login' error message.

        pass
    return render(request, "authorization.html")


def artist_list(request):
    return render(request, "artist_list.html", {'artists': Artist.objects.all()})

def employee_list(request):
    return render(request, "employee.html", {'employees': Employee.objects.all()})


def listexpo(request):
    return render(request, "ListExpo.html", {'expo': Expo.objects.all()})

def countrySearch(request):
    return render(request, "country.html", {'countries': Country.objects.all()})


