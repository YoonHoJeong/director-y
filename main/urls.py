from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('directors/', views.directors, name="directors"),
    path('movie_detail/<int:movie_id>', views.movie_detail, name="movie_detail"),
    path('staffs/', views.staffs, name='staffs'),
    path('actors/', views.actors, name='actors'),
    path('actor_detail/<int:actor_id>',
         views.actor_detail, name='actor_detail'),
    path('new/', views.new, name="new"),
    path('staff_detail/<int:staff_profile_id>',
         views.staff_detail, name='staff_detail'),
    path('section_create/', views.section_create, name="section_create"),
    path('section/', views.section, name="section"),
    path('enroll_movie/', views.enroll_movie, name="enroll_movie"),
    path('movie/', views.movie, name="movie"),
    path('section_detail/<int:section_id>', views.section_detail, name='section_detail'),
    path('update_movie/<int:movie_id>', views.update_movie, name='update_movie'),
    path('delete_movie/<int:movie_id>', views.delete_movie, name='delete_movie'),
    path('section_update/<int:section_id>', views.section_update, name='section_update'),
    path('section_delete/<int:section_id>', views.section_delete, name='section_delete'),
]
