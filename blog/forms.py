import re

from django import forms  # создание форм Django (docs)
from django.core.validators import ValidationError

from .models import BlogPost


class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'subtitle', 'body', 'category']
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
