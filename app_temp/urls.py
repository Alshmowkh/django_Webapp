from django.urls import path
# from app_temp import views
from . import views
from .views import ArticleListView, ArticleDetailView


urlpatterns=[
    path('students/', views.students, name='students'),
    path('students/<int:id>', views.student, name='student'),
    path("index", views.index, name='index'),
    path("tempHTML/", views.tempHTML, name='tempHTML'),
    path("simple_form/", views.form, name='form'),
    path("",ArticleListView.as_view(), name='article_list'),
    path("<int:pk>", ArticleDetailView.as_view(), name='article_detail'),
    
   
]