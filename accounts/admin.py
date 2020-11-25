from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Director, Actor, Staff, SNS


# Register your models here.

class ProfileAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined',
                    'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'name', 'password1', 'password2', 'u_type', 'is_staff', 'is_active')}
        ),
    )


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(Staff)
admin.site.register(SNS)
