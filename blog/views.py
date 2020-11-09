import requests
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from .forms import PostForm
from .models import BlogPost, Category


class HomePage(ListView):
    model = BlogPost
    template_name = 'blog/home.html'
    context_object_name = 'object_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        api_url = 'https://api.openweathermap.org/data/2.5/weather?q=Minsk&units=metric&appid=fe6c9ac08e96ecdd33f559f07bc59da7'
        res = requests.get(api_url)  # погода в Минске в настоящее время
        data = res.json()
        context['temp'] = data['main']['temp']
        return context


def category_view(request, category_id):
    news = BlogPost.objects.filter(category_id=category_id)  # добавляет условие? (фильтр), cat_id принимает в urls
    category_id = Category.objects.get(pk=category_id)  # получаем из БД категорию по её pk, где ключ = category_id
    return render(request, 'blog/category.html',
                  {'news': news, 'category': category_id})


def add_post(request):
    if request.method == "POST":  # отправляем форму в БД
        form = PostForm(request.POST)  # or PostFormExample(request.POST)
        if form.is_valid():  # прошла ли форма валидацию
            post = BlogPost.objects.create(**form.cleaned_data)  # распакуем словарь и доваим в БД
            # post = form.save() --> в случае использовании BlogPostExample
            return redirect(post)
    else:  # генерируем страницу формы
        form = PostForm()
    return render(request, 'blog/add_post.html', {'form': form})


def view_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog/read_article.html', {"post_item": post})


def about_view(request):
    category = Category.objects.all()
    template_name = 'blog/about.html'
    return render(request, template_name)


def contact(request):
    category = Category.objects.all()
    template_name = 'blog/contact.html'
    return render(request, template_name)
