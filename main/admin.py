from django.contrib import admin

from .models import Movie, Festival, Section, SPortfolio, ActorImage, ActorVideo, Genre, Filmography

# Register your models here.
admin.site.register(Movie)
admin.site.register(Festival)
admin.site.register(Section)
admin.site.register(SPortfolio)
admin.site.register(ActorImage)
admin.site.register(ActorVideo)
admin.site.register(Genre)
admin.site.register(Filmography)
