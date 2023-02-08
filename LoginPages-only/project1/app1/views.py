from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog

def home(request):
    post=Blog.objects.all()

    return render(request, "base.html",{'post':post})
def demo(requset):
    name = "12345"
    post=Blog.objects.all()
    return HttpResponse("<html><body><h2>my name is"+ post.author+"<u>vinay</u> kumar</h2></body></html>")
# Create your views here.
