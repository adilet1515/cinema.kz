from django.contrib.auth.models import User
from django.db import models



class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Film(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    genres = models.ManyToManyField(Genre, related_name='films')
    director = models.CharField(max_length=200)
    poster = models.ImageField(upload_to='films')
    posted_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


