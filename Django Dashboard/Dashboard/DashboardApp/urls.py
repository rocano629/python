from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from DashboardApp import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    url(r"^Dashboard/api/chart/data/$", views.ChartData.as_view(), name="api-data"),
    
]