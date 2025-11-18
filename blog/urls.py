from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog', views.blog.as_view(), name='blog'),
    path('post-edit/<slug:slug>/', views.editpost, name='edit-post'),
    path('contact', views.contact, name='contact'),
    path('profile/', views.profile, name='users-profile'),
    path('<slug:slug>/', views.post_blog, name='post_blog'),
]