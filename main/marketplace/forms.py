from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl'


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    username = forms.CharField(widget=forms.TimeInput(attrs={
        'placeholder': 'Введіть ваше ім\'я',
        'class': INPUT_CLASSES
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Введіть вашу електронну адресу',
        'class': INPUT_CLASSES
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Введіть ваш пароль',
        'class': INPUT_CLASSES
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Введіть ваш пароль ще раз ',
        'class': INPUT_CLASSES
    }))


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TimeInput(attrs={
        'placeholder': 'Введіть ваше ім\'я',
        'class': INPUT_CLASSES
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Введіть ваш пароль',
        'class': INPUT_CLASSES
    }))
