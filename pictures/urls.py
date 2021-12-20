from django.contrib import admin
from django.urls import path, include
from pictures.views import *

urlpatterns = [
    path('', index),


    path('authorization',authorization), #https://djbook.ru/rel1.9/topics/auth/default.html

    path('employee', employee_list),
    path('addpictures', index2),

    #path('listofartists', artist_list)
]


