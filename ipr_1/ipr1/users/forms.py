from datetime import date

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from users.models import Profile, CustomUser


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'birth_date', 'password1', 'password2']



    def clean_birth_date(self):
        birth_date = self.cleaned_data['birth_date']
        today = date.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

        if age < 18:
            raise ValidationError("Регистрация возможна только для пользователей старше 18 лет.")

        return birth_date

    def save(self, commit=True):
        user = super().save(commit=False)  # Не сохраняем еще пользователя
        user.email = self.cleaned_data['email']  # Устанавливаем email
        if commit:
            user.save()  # Сохраняем пользователя в базе данных
        return user


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']