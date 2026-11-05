from django.contrib import admin
from .models import Director, Actor, Genre, Movie, Rating, Review

admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Rating)
admin.site.register(Review)
