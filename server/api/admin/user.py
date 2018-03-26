from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from server.api.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    personal_info = UserAdmin.fieldsets[1][1]['fields'] + (
      'age',
      'gender',
    )
    UserAdmin.fieldsets[1][1]['fields'] = personal_info
    fieldsets = UserAdmin.fieldsets
