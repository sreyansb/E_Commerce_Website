from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog
# Create your views here.
def index(request):
    allblogs=Blog.objects.all()
    return render(request,"blog/index.html",{'allblogs':allblogs})

def blogpost(request,id):
    allblogs=Blog.objects.get(post_id=id)
    yespr=0
    yesne=0
    prevtitle=""
    nexttitle=""
    previd=0
    nextid=0
    if id>1:
        yespr=1
        prevtitle=Blog.objects.get(post_id=id-1).title
        previd=id-1
    if id<len(Blog.objects.all()):
        yesne=1
        nexttitle=Blog.objects.get(post_id=id+1).title
        nextid=id+1
    params={'allblogs':allblogs,"previd":previd,"nextid":nextid,"yespr":yespr,"yesne":yesne,"prevtitle":prevtitle,"nexttitle":nexttitle}
    return render(request,"blog/blogpost.html",params)
