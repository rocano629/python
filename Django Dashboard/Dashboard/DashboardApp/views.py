from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import View
import pyodbc 
import pandas as pd
import plotly.graph_objects as go
# Create your views here.

class HomeView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'index.html')

class ChartData(APIView):

    authentication_classes=[]
    permission_classes = []

    def get(self, request, format=None):
        conn = pyodbc.connect('Driver={SQL Server};'
        'Server=DESKTOP-U688F7I;'
        'Database=AdventureWorks2017;'
        'Trusted_Connection=yes;')

        SQL_Query = pd.read_sql_query('SELECT TOP (6) [CustomerID] FROM [AdventureWorks2017].[Sales].[Customer]', conn)

        df = pd.DataFrame(SQL_Query, columns=['CustomerID'])

        default_items= df['CustomerID'].tolist()
        data={
        "sales":100,
        "default":default_items,
        }
        return Response(data)

def get_data(request,*args,**kwargs):
    data={
        "sales":100,
        "Customers":10,

    }
    return JsonResponse(data)


