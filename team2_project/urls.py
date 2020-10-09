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
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('accounts.urls')),
    path('summernote/', include('django_summernote.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
