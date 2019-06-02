from django.urls import path,include
from forms_app import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^forms', views.form, name='form'),
    url(r'^users',views.index,name='users'),
    url(r'^help',views.form,name='Help'),    
]