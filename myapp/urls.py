from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('article/new/', views.create_article, name='create_article'),
    path('search/', views.search_articles, name='search_articles'),
     path('article/<int:article_id>/', views.article_detail, name='article_detail'),

]


