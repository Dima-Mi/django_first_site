from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView

from .forms import PostForm, UserRegisterForm, UserLoginForm
from .models import BlogPost, Category


class HomePage(ListView):
    paginate_by = 6
    model = BlogPost  # от куда берем данные
    template_name = 'blog/home.html'  # шаблон
    context_object_name = 'object_list'  # название переменной в шаблоне
    queryset = BlogPost.objects.all().select_related('category')[1:]

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['popular'] = BlogPost.objects.all().select_related('category')[0]  # главная новость (по новизне)
        return context


class CategoryView(ListView):  # ListView для list-объектов
    model = BlogPost
    template_name = 'blog/category.html'
    context_object_name = 'news'
    allow_empty = False  # если пустая категория -> 404
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):  # что надо выводить (фильтрует)
        return BlogPost.objects.filter(category_id=self.kwargs['category_id']).select_related('category')


class AddPost(LoginRequiredMixin, CreateView):  # CreateView для форм
    form_class = PostForm
    template_name = 'blog/add_post.html'
    login_url = '/'


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


def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'blog/login.html', {"form": form})


def user_logout(request):
    logout(request)
    return redirect('home')
