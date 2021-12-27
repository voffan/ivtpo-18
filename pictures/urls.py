from django.contrib import admin
from django.urls import path
from pictures.views import *

urlpatterns = [
    path('', index, name='index'),

    path('authorization', authorization),

    path('employee', employee_list),

    path('listexpo', listexpo),

    path('country', countrySearch),

    path('listofartists', artist_list)
]


