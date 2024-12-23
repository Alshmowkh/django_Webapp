from django.contrib import admin

# Register your models here.
from .models import Article, Student

admin.site.register(Student)

class ArticleAdmin(admin.ModelAdmin):
    list_display=("title","body")

admin.site.register(Article, ArticleAdmin)