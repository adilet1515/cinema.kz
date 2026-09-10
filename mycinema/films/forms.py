from tkinter import Listbox

from django.forms import ModelForm, CharField, TextInput, Textarea, SelectMultiple
from .models import Film, Genre


class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'description', 'poster', 'genres' , 'director']
        widgets = {
            'title': TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Введите название фильма',}
            ),
            'description': Textarea(
                attrs={'class': 'form-control',
                       'placeholder':'Описание фильма'}
            ),
            'genres': SelectMultiple(
                attrs={
                    'class': 'form-control',
                    'id': 'genre-select',
                }
            ),
        }







class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'

