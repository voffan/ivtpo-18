from django.contrib import admin
from django.urls import path
from pictures.views import *

urlpatterns = [
    path('', index),
    path('authorization',authorization),
]