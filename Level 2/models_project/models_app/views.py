from django.shortcuts import render

# Create your views here.

def index(request):
    my_dic ={'insert_content' : "Hello this is the models app"}

    return render(request,"models_app/index.html",context=my_dic)