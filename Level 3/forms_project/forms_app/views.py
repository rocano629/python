from django.shortcuts import render
from forms_app import forms
# Create your views here.

def index(request):
    return render(request,'forms_app/index.html')

def form(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("Validation Success")
            print("Name "+form.cleaned_data['name'])
            print("Email "+form.cleaned_data['email'])
            print("Test "+form.cleaned_data['text'])

    return render(request,'forms_app/forms.html',{'form':form})
