from django.db.models import IntegerField
from .models import Picture
from .models import *
from django.forms import ModelForm, TextInput, DateInput
from django.forms import ModelChoiceField
from django import forms
from django.db import models


class AuthorSelect(forms.Select):
    def create_option(self, *args, **kwargs):
        option = super().create_option(first_name, last_name)
        if value:
            option['first_name'] = value.instance.first_name + value.instance.last_name
        return option

class GallerySelect(forms.Select):
    def create_option(self, *args, **kwargs):
        option = super().create_option(name)
        if value:
            option['gallery'] = value.instance.name
        return option

class PlacementSelect(forms.Select):
    def create_option(self, *args, **kwargs):
        option = super().create_option(name)
        if value:
            option['placement'] = value.instance.name
        return option

class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ['name', 'author', 'year', 'cost', 'placement', 'status', 'gallery']
        widget = {
		'author': AuthorSelect,
		'gallery': GallerySelect,
		'placement': PlacementSelect
		}



    ##    widgets = {
    ##        "name": TextInput(attrs={
    ##           'class': 'form-control',
    ##        }),
    ##		 "author": TextInput(attrs={
    ##           'class': 'form-control',
    ##       }),
    ##		 "year": DateInput(attrs={
    ##           'class': 'form-control',
    ##       }),
    ##		 "cost": TextInput(attrs={
    ##        'class': 'form-control',
    ##       }),
    ##		 "placement": TextInput(attrs={
    ##           'class': 'form-control',
    ##       }),
    ##		 "status": TextInput(attrs={
    ##            'class': 'form-control',
    ##        }),
    ##		"gallery": TextInput(attrs={
    ##           'class': 'form-control',
    ##       })
    ##   }
