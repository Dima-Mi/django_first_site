import re

from ckeditor.widgets import CKEditorWidget
from django import forms  # создание форм Django (docs)
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.validators import ValidationError

from .models import BlogPost


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя',
                               help_text='Имя пользователя должно состоять максимум из 150 символов',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class PostForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget(), label='Основыной текст')

    class Meta:
        model = BlogPost
        fields = ['title', 'subtitle', 'body', 'photo', 'category']  # кто будет отображаться и в каком порядке
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'subtitle': forms.TextInput(attrs={"class": "form-control"}),
            'body': forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            'category': forms.Select(attrs={"class": "form-control"}),

        }

    def clean_title(self):  # собственный валидатор на поиск несоответствий
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Заголовок не должен начинаться с цифры')
        return title
