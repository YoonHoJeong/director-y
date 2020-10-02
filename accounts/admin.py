from django.contrib import admin
from .models import Profile, Director, Actor, Staff

# Register your models here.

admin.site.register(Profile)
admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(Staff)
