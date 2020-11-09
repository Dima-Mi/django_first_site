from django.contrib import admin
from .models import BlogPost, Category


class BlogPostAdmin(admin.ModelAdmin):  # настройка "отображения" BlogPost в админке
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at')  # что будет отображено в админке
    list_display_links = ('id', 'title')  # кто будет ссылкой  в админке
    search_fields = ('title', 'body')  # создает поиск и будет искать по выбранным полям
    list_filter = ('category',)  # создает фильтр по выбранным полям
    # list_editable = () --- создает возможность редактировать не заходя в пост (отмечать публикацию)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(BlogPost, BlogPostAdmin)  # добавление в админку пункта BlogPost и присваивание BlogPostAdmin
admin.site.register(Category, CategoryAdmin)
