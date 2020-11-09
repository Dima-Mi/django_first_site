from django import template

from blog.models import Category

register = template.Library()  # необходимая строчка


@register.simple_tag(name='categories_list')  # тег возвращает данные
def get_categories():  # создание функции получения категорий (что бы не писать в views каждый раз)
    return Category.objects.all()  # вызывается {% load blog_tags %} и {% get_categories as category %}


@register.inclusion_tag('base.html')  # __ПРИМЕР__, в проекте не используется
def show_categories():
    categories = Category.objects.all()  # возвращаем dict в blog/home.html и там производим операции
    return {'categories': categories}  # вызов через {% show_categories %}
