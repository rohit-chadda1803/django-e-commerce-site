from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost
# Create your views here.
def index(request):
    blogs = Blogpost.objects.all()
    blogposted = {'blogs':blogs}
    #print(blogposted)
    return render(request,'blog/index.html',blogposted)
    #return HttpResponse("<h1>this is index of blog.</h1>")

def blogpost(request,myid):
    blog = Blogpost.objects.filter(post_id=myid)
    blogposted = {'blog':blog[0]}
    #print(blogposted)
    return render(request,'blog/blogpost.html',blogposted)
    #return HttpResponse("<h1>this is index of blog.</h1>")