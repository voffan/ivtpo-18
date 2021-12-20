from django.contrib import admin
from django.urls import path
from pictures.views import *

urlpatterns = [
    path('', index),


    path('authorization',authorization),

    path('employee', employee_list),


    path('listofartists', artist_list)
]


