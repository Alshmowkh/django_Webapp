from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView, DeleteView
from .models import Article, Student
from django.template import loader
from .myfunctions import members, test
from django.http import HttpRequest
import requests
from django.views.decorators.csrf import csrf_exempt
from .forms import Formy

# Create your views here.
# print(dir(render))


@csrf_exempt
def students(request):
    var = "txt1" in request.POST
    sts = Student.objects.all
    context = {"students": sts, "var": var, "formy": Formy}
    return render(request, "students.html", context)


def student(request, id):
    usr = request.user.is_authenticated
    usr = request.user.is_anonymous
    # usr= request.META.HTTP_REFERER
    # usr=request.auser

    # if request.user.username == 'alshmowkh':
    st = Student.objects.get(student_ID=id)
    return render(request, "student.html", {"student": st})
    # else:
    # return HttpResponse(f'<h1 style="color:red;text-align:center;margin:200px">Forbidden URL!{usr}<h1>')


def index(request):
    # return HttpResponse("Yes")
    return redirect("article_list")


def jen(request):
    return render(request, "jen.html", {"a": "B"})


def getSymmetricKey():
    import secrets

    return secrets.token_bytes(40)  # .hex()


def tempHTML(request):

    list="hello"
    # template=loader.get_template("tempHTML.html")
    # return HttpResponse(template.render())
    # return render(request,'tempHTML.html',{'c':'C'})
    # print(request)

    # list1=dir(ListView)
    # return render(request,'tempHTML.html',{'a':'B','Z':'z','list':list1})

    # api_url = "https://restcountries.com/v3.1/currency/eg"
    x = "A"
    list = []
    # x=requests.get(api_url)
    # x=type(x)
    # list=members(request.META)
    # list =x.json()

    # list = dir(request.user)
    # list=request.headers
    # x = request.headers.HTTP_PREFIX
    # x = getSymmetricKey()
    dicty = {}

    response = {"list": list, "var": x, "dict": dicty}
    return render(request, "tempHTML.html", response)


def form(request):
    inpt = request.GET.get("txt_field")
    xss = "<script>alert('I am xss attack!');</script>"
    xss = type(request.COOKIES)
    return render(request, "simple_form.html", {"data1": "yes", "xss": xss})


class ArticleListView(ListView):
    model = Article
    template_name = "article_list.html"


class ArticleDetailView(DeleteView):
    model = Article
    template_name = "article_detail.html"
