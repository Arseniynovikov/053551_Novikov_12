from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from users.models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)  # Не сохраняем еще пользователя
        user.email = self.cleaned_data['email']  # Устанавливаем email
        if commit:
            user.save()  # Сохраняем пользователя в базе данных
        return user


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']