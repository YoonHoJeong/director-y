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

]
