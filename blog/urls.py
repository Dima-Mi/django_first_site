from django.urls import path

from . import views

urlpatterns = [

    path('', views.HomePage.as_view(), name='home'),
    path('category/<int:category_id>/', views.category_view, name='category'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact, name='contact'),
    path('post/<int:pk>/', views.view_post, name='post_detail'),
    path('add-post/', views.add_post, name='add_post')
]
