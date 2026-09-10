from django.urls import path
from .views import index, CreateFilmView, CreateGenresView, FilmsListView, GenreDetailView, FilmDetailView, \
    FilmUpdateView

app_name = 'films'

urlpatterns = [
    path("index/", index, name="index"),
    path("create/", CreateFilmView.as_view() , name="create"),
    path("create/genre/", CreateGenresView.as_view() , name="create_genre"),
    path("", FilmsListView.as_view() , name="list"),
    path("genre/<int:pk>", GenreDetailView.as_view() , name="genre_detail"),
    path("detail/<int:pk>", FilmDetailView.as_view() , name="detail"),
    path("update/<int:pk>", FilmUpdateView.as_view() , name="update"),
]