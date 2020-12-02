from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


from main import views
from accounts.views import (
    register,
    logout_view,
    login_view,
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
<<<<<<< HEAD
    add_like,
    delete_like,
    add_like_movie,
    delete_like_movie,
=======
    staff_update,
    staff_delete,
    staff_create,
>>>>>>> 7d71797c221b5f7ccf2ed8780ece0776f7960b29
)

urlpatterns = [
    path('register/', register, name="register"),
    path('logout/', logout_view, name="logout"),
    path('login/', login_view, name="login"),
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
    path('add_like_movie', add_like_movie, name="add_like_movie"),
    path('delete_like_movie', delete_like_movie, name="delete_like_movie"),
    path('add_like', add_like, name="add_like"),
    path('delete_like', delete_like, name="delete_like"),
    path('staff_update/<int:portfolio_id>', staff_update, name="staff_update"),
    path('staff_delete/<int:portfolio_id>', staff_delete, name="staff_delete"),
    path('staff_create', staff_create, name='staff_create'),
]
