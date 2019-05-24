from django.conf.urls import url
from models_app import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
]