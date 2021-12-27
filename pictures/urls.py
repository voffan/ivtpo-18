from django.contrib import admin
from django.urls import path
from pictures.views import *

urlpatterns = [
    path('', index),

    path('picture', piclist, name="addpicture"),

    path('authorization', authorization),

    path('employee', employee_list),

    path('listexpo', listexpo),

    path('listofartists', artist_list),

    path('genre_search', genre_search),

    path('country_list', country_list),

    path('picture_detail/<int:picture_id>', picture_detail, name='picture_detail')
]

