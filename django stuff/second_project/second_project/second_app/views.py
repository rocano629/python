from django.shortcuts import render
from django.http import HttpResponse
from second_app.forms import NewUserForm
#from second_app.models import User
# Create your views here.


def index(request):
    #return HttpResponse("<em>Hello World 2</em>")
    return render(request,'second_app/index.html')

def help(request):
    #return HttpResponse("<em>Hello World 2</em>")
    my_dict = {'insert_me':"Help page with template tag"}

    return render(request,'second_app/help.html',context =my_dict)

#def users(request):
    #return HttpResponse("<em>Hello World 2</em>")
    #my_dict = {'users':"Users page"}
 #   user_list = User.objects.order_by('FirstName')
 #   user_dict = {'users':user_list}
    

  #  return render(request,'second_app/users.html',context =user_dict)

def users(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit = True)
            return index(request)
        else:
            print('ERROR FORM INVALID')
    return render(request,'second_app/users.html',{'form':form})
