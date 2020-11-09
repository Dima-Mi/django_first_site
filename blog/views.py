import requests
from django.views.generic import ListView, DetailView, CreateView

from .forms import PostForm
from .models import BlogPost, Category


class HomePage(ListView):
    model = BlogPost  # от куда берем данные
    template_name = 'blog/home.html'  # шаблон
    context_object_name = 'object_list'  # название переменной в шаблоне

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        api_url = 'https://api.openweathermap.org/data/2.5/weather?q=Minsk&units=metric&appid=fe6c9ac08e96ecdd33f559f07bc59da7'
        res = requests.get(api_url)  # погода в Минске в настоящее время
        data = res.json()
        context['temp'] = data['main']['temp']  # добавление в общий context - temp (исп в шаблоне html)
        return context


class CategoryView(ListView):  # ListView для list-объектов
    model = BlogPost
    template_name = 'blog/category.html'
    context_object_name = 'news'
    allow_empty = False  # если пустая категория -> 404

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):  # что надо выводить (фильтрует)
        return BlogPost.objects.filter(category_id=self.kwargs['category_id'])


class AddPost(CreateView):  # CreateView для форм
    form_class = PostForm
    template_name = 'blog/add_post.html'


class PostView(DetailView):  # DetailView для определенного объекта
    model = BlogPost
    template_name = 'blog/read_article.html'
    context_object_name = 'post_item'
    allow_empty = False


class AboutView(ListView):
    model = Category
    template_name = 'blog/about.html'


class ContactView(ListView):
    model = Category
    template_name = 'blog/contact.html'
