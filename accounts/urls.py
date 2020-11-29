from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


from main import views
from accounts.views import (
    register,
    registration_view,
    logout_view,
    login_view,
    actor_register,
    director_register,
    staff_register,
    user_page,
    edit_user,
    my_account,
    edit_password,
    delete_actor_image,
    add_actor_image,
    likes,
    likes_director,
    likes_actor,
    likes_staff,
)

urlpatterns = [
    path('register/', register, name="register"),
    path('logout/', logout_view, name="logout"),
    path('login/', login_view, name="login"),
    path('actor_register/', actor_register.as_view(), name="actor_register"),
    path('director_register/', director_register.as_view(),
         name="director_register"),
    path('staff_register/', staff_register.as_view(), name="staff_register"),
    path('user_page/<int:user_id>', user_page, name="user_page"),
    path('user_page/', user_page, name="user_page"),
    path('edit_user/', edit_user, name="edit_user"),
    path('add_actor_image/', add_actor_image, name="add_actor_image"),
    path('delete_actor_image/<int:image_id>', delete_actor_image, name="delete_actor_image"),
    path('my_account/', my_account, name="my_account"),
    path('my_account/edit_password', edit_password, name="edit_password"),
    path('my_account/likes', likes, name="likes"),
    path('my_account/likes/director', likes_director, name="likes_director"),
    path('my_account/likes/actor', likes_actor, name="likes_actor"),
    path('my_account/likes/staff', likes_staff, name="likes_staff"),
]
