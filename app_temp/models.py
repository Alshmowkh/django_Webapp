from django.db import models
from django.urls import reverse

# Create your models here.

class Article(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField()

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("article_detail",args=[self.id])
class Student(models.Model):
    student_ID=models.IntegerField(primary_key=True)
    student_name=models.CharField(max_length=25)#, widget=forms.TextInput(atrrs={'class': 'form-control'}))
    dept_choice=(
        ('cs','CS'),
        ('is','IS'),
        ('it','IT'),
        ('cys','CYS'),
        ('ds','DS'),
        ('ai','AI'),
    )
    student_dept=models.CharField(max_length=3,choices=dept_choice,default='cys')
    student_img=models.FileField(upload_to="images/",blank=True)
    def __str__(self):
        return self.student_name