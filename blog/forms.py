import re

from django import forms  # создание форм Django (docs)
from django.core.validators import ValidationError

from .models import Category, BlogPost


class PostFormExample(forms.Form):
    title = forms.CharField(max_length=150, label="Заголовок", widget=forms.TextInput(attrs={"class": "form-control"}))
    subtitle = forms.CharField(max_length=150, label="Подзаголовок",
                               widget=forms.TextInput(attrs={"class": "form-control"}))
    body = forms.CharField(label="Основной текст",
                           widget=forms.Textarea(attrs={
                               "class": "form-control",
                               "rows": 5
                           }))  # label - для пользователей
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория',
                                      empty_label="Выберите категорию", widget=forms.Select(
            attrs={"class": "form-control"}))  # empty_label - вместо "---------"


class PostForm(forms.ModelForm):  # /\ пример индетичный PostFormExample выше /\
    class Meta:
        model = BlogPost
        fields = ['title', 'subtitle', 'body', 'category']
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'subtitle': forms.TextInput(attrs={"class": "form-control"}),
            'body': forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            'category': forms.Select(attrs={"class": "form-control"})
        }

    def clean_title(self):  # собственный валидатор на поиск несоответствий
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Заголовок не должен начинаться с цифры')
        return title
