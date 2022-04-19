from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from role.models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'user_type', 'is_staff',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2','user_type'),
        }),
    )
admin.site.register(CustomUser, CustomUserAdmin)