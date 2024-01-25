from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from users.models import User


class UserRegisterForm(UserCreationForm):
    """Форм-класс формы регистрации пользователя"""
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    """Форм-класс профиля пользователя"""
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()