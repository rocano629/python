from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("<em>Hello World 2</em>")

def help(request):
    #return HttpResponse("<em>Hello World 2</em>")
    my_dict = {'insert_me':"Help page with template tag"}

    return render(request,'second_app/help.html',context =my_dict)
