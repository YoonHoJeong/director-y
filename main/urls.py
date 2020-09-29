from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('actors/', views.home_actor, name='home_actor'),
    path('staffs', views.home_staff, name='home_staff'),
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
]
