from django.contrib import admin
from django.urls import path
from pictures.views import *

urlpatterns = [
    path('', index),
    path('picture', piclist, name="addpicture"),
    path('employee', employee_list),
    path('addpictures', index2),
]