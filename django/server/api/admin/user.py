from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import (
    UserCreationForm, UserChangeForm
)
from django import forms

from server.api.models import User


class CustomUserCreationForm(UserCreationForm):
    bio = forms.CharField(
        max_length=140,
        widget=forms.Textarea,
    )

    class Meta(UserCreationForm.Meta):
        model = User


class CustomUserChangeForm(UserChangeForm):
    bio = forms.CharField(
        max_length=140,
        required=False,
        widget=forms.Textarea,
    )

    class Meta(UserChangeForm.Meta):
        model = User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'display_name',
        'is_staff',
    )

    personal_info = UserAdmin.fieldsets[1][1]['fields'] + (
      'display_name',
      'birth_date',
      'gender',
      'bio',
    )
    UserAdmin.fieldsets[1][1]['fields'] = personal_info

    permissions = (
      'hidden',
    ) + UserAdmin.fieldsets[2][1]['fields']
    UserAdmin.fieldsets[2][1]['fields'] = permissions
    fieldsets = UserAdmin.fieldsets
