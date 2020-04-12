from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import View
import pyodbc 
import pandas as pd
import plotly.graph_objects as go
from DashboardApp.models import Salesreport
# Create your views here.

class HomeView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'DashboardApp/index.html')

class ChartData(APIView):

    authentication_classes=[]
    permission_classes = []

    def get(self, request, format=None):

        df = pd.DataFrame(list(Salesreport.objects.all().values()))
        # df = pd.DataFrame(SQL_Query, columns=['2014'])
        
        Total2011 = df['number_2011'].sum()
        Total2012 = df['number_2012'].sum()
        Total2013 = df['number_2013'].sum()
        Total2014 = df['number_2014'].sum()

        default_items= [Total2011,Total2012,Total2013,Total2014]#df['number_2014'].tolist()
        data={
        "sales":100,
        "default":default_items,
        }
        return Response(data)

# def get_data(request,*args,**kwargs):
#     data={
#         "sales":100,
#         "Customers":10,

#     }
#     return JsonResponse(data)


