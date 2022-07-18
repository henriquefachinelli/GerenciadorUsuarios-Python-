from dataclasses import fields
from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from .forms import UserCreationForm,UserChangeForm
from .models import User

@admin.register(User)

class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = User
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        ("Empresa o qual pertence", {"fields": ("grupo",)}),
    )
