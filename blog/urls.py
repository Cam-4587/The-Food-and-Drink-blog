from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog', views.blog.as_view(), name='blog'),
    path('<slug:slug>/', views.post_blog, name='post_blog'),
]