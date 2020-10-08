from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('directors/', views.directors, name="directors"),
    path('staffs/', views.staffs, name='staffs'),
    path('actors/', views.actors, name='actors'),
    path('mypage/', views.mypage, name='mypage'),
    path('new/', views.new, name="new"),
    path('staff_detail/<int:staff_profile_id>', views.staff_detail, name='staff_detail'),
    path('actordetail/<int:actor_profile_id>', views.actordetail, name='actordetail'),
]
