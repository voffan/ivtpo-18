from django.contrib import admin
from django.urls import path
from pictures.views import *

urlpatterns = [
    path('', index),
    path('employee', employee_list),
    path('addpictures', index2),
    path('genre_search', genre_search)
]