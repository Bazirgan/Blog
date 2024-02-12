from django.shortcuts import render,HttpResponse
from .models import Article
def index(request):
    return render(request,"index.html")


def about(request):
    return render(request,"about.html")




def articles(request):
    keyword = request.GET.get("keyword")

    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        return render(request,"articles.html",{"articles":articles})
    articles = Article.objects.all()

    return render(request,"articles.html",{"articles":articles})