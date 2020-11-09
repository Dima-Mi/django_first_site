from django.db import models
from django.urls import reverse


class BlogPost(models.Model):  # про Field(поля) есть отличная документация на оф сайте
    # id - django автоматически присвает id
    title = models.CharField(max_length=120, null=True, blank=False, verbose_name='Заголовок')
    subtitle = models.CharField(max_length=180, null=True, blank=False, verbose_name='Подзаголовок')
    body = models.TextField(verbose_name='Текст')
    photo = models.ImageField(upload_to='photo/%Y/%m/%d', blank=True,  # если True, значит поле необязательное
                              verbose_name='Фото')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    category = models.ForeignKey(  # создаём связь многие (посты) к одному (класс Category)
        'Category',  # можно писать без ковычек, если класс определён первым
        on_delete=models.PROTECT, null=True, verbose_name='Категория'
    )

    def get_absolute_url(self):  # абсолютная ссылка
        return reverse('post_detail', kwargs={'pk': self.pk})

    def __str__(self):  # отображение текста title в /admin вместо BlogPost
        """Строковое отображение модели"""
        return self.title[:50]

    class Meta:  # Настройка 'отображения'
        verbose_name = 'Пост'  # имя в админке
        verbose_name_plural = 'Посты'  # имя в админке на множественное
        ordering = ['-created_at']  # сортировка по выбранному полю (знак "-" значит reverse-порядок)


class Category(models.Model):
    title = models.CharField(max_length=50, db_index=True,  # присваивание индекса в СУБД (облегчает поиск)
                             verbose_name='Наименование категории')

    def get_absolute_url(self):  # абсолютная ссылка
        return reverse('category', kwargs={'category_id': self.pk})

    def __str__(self):
        """Строковое отображение модели"""
        return self.title

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
        ordering = ['id']
