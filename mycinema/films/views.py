from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, request, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Film, Genre
from .forms import FilmForm, GenreForm
# Create your views here.


def index(request:HttpRequest):
    films = ['adilet',
             'bydyk',
             'tulki']

    context = {'films':films}
    return render(request, 'films/index.html', context)

class CreateFilmView(LoginRequiredMixin,CreateView ):
    model = Film
    form_class = FilmForm
    template_name = 'films/create_film.html'
    success_url = '/films/create/genre/'
    def form_valid(self, form):
        film = form.save(commit=False)
        film.author = self.request.user
        film.save()
        return super().form_valid(form)

    def handle_no_permission(self):
        return HttpResponse("You are not allowed to use this view")


class CreateGenresView(LoginRequiredMixin,CreateView ):
    model = Genre
    form_class = GenreForm
    success_url = '/films/create/genre/'

class FilmsListView(ListView):
    model = Film
    context_object_name = 'films'

class GenreDetailView(DetailView):
    model = Genre
    context_object_name = 'genre'
    template_name = 'films/genre_detail.html'

class FilmDetailView(DetailView):
    model = Film
    context_object_name = 'film'
    template_name = 'films/film_detail.html'


class FilmUpdateView(LoginRequiredMixin, UpdateView):
    model = Film
    form_class = FilmForm
    template_name = 'films/film_edit.html'

    def get_queryset(self):
        return Film.objects.filter(author=self.request.user)

    def get_success_url(self):
        return reverse_lazy(
            'films:detail',
            kwargs={'pk': self.object.pk}
        )





