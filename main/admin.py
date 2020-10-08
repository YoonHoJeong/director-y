from django.contrib import admin

from .models import Movie, Festival, Section, SPortfolio, ActorImage, ActorVideo

# Register your models here.
admin.site.register(Movie)
admin.site.register(Festival)
admin.site.register(Section)
admin.site.register(SPortfolio)
admin.site.register(ActorImage)
admin.site.register(ActorVideo)
