from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'first_name', 'last_name','manzil',  'age', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age','manzil',)}),
    )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('age','manzil',)}),
    )
    
admin.site.register(CustomUser, CustomUserAdmin)
