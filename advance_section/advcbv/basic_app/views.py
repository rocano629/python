from django.shortcuts import render
from django.views.generic import View,TemplateView
from django.http import HttpResponse

# Create your views here.

#def index(request):
#    return render(request,'index.html')

#class CBView(View):
#    def get(self,request):
#        return HttpResponse("Class Based Views are Cool")

class IndexView(TemplateView):
    template_name = 'index.html'