from django.test import TestCase

from .models import BlogPost


class SimpleTest(TestCase):  # создание теста на доступность по коду 200/302
    def test_admin_page_status_code(self):
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 302)

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_contact_page_status_code(self):
        response = self.client.get('/add-post/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_contact_page_status_code(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)


class PostModelTest(TestCase):  # тест на доступность создания текса в BlogPost

    def setUp(self):  # создание примера для сравнения
        BlogPost.objects.create(body='just a test')

    def test_text_content(self):  # сравнение примера (проверка создался ли текст)
        post = BlogPost.objects.get(id=1)
        expected_object_name = f'{post.body}'
        self.assertEqual(expected_object_name, 'just a test')
