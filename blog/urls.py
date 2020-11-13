from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('category/<int:category_id>/', views.CategoryView.as_view(), name='category'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('post/<int:pk>/', views.PostView.as_view(), name='post_detail'),
    path('add-post/', views.AddPost.as_view(), name='add_post')
]

