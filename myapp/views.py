'''from django.shortcuts import render , render_to_response

# Create your views here.
def index(requests):
    return render_to_response['index.html']'''




from django.http import JsonResponse
# import matplotlib
# matplotlib.use('Agg')
# import matplotlib.pyplot as plt
# import io 
# import urllib,base64

from django.views.generic import TemplateView
import pandas as pd
from django.shortcuts import render
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
import numpy as np

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'chart.html')

def get_data(request, *args, **kwargs):
    df=pd.read_excel("data.xlsx")
    df=df.dropna()
    dr=df["Profitto/Perdita (€)"].tolist()
    dr.reverse()
    ndr=list(np.cumsum(dr))
    ide = list(range(len(ndr)))
    #res = {ide[i]: round(float(ndr[i]),2) for i in range(len(ide))}
    data ={
        "ids":ide,
        "chartdata":ndr
    }
    return JsonResponse(data) # http response

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []
   
    def get(self, request, format = None):
        labels = [
            'January',
            'February', 
            'March', 
            'April', 
            'May', 
            'June', 
            'July'
            ]
        chartLabel = "my data"
        chartdata = [0, 10, 5, 2, 20, 30, 45]
        data ={
                     "labels":labels,
                     "chartLabel":chartLabel,
                     "chartdata":chartdata,
             }
        return Response(data)




def index(request):
    context = {'foo': 'bar'}
    return render(request, 'index.html', context)   
    
def about(request):
    context = {'foo': 'bar'}
    return render(request, 'about.html', context)   

def contact(request):
    context = {'foo': 'bar'}
    return render(request, 'contact.html', context)   
def jobs(request):
    context = {'foo': 'bar'}
    return render(request, 'jobs.html', context)   
def lab(request):
    context = {'foo': 'bar'}
    return render(request, 'lab.html', context)   
def login(request):
    context = {'foo': 'bar'}
    return render(request, 'login.html', context)   
def solutions(request):
    context = {'foo': 'bar'}
    return render(request, 'solutions.html', context)   
def trading_methodology(request):
    context = {'foo': 'bar'}
    return render(request, 'trading_methodology.html', context)   
def trading_strategy(request):
    context = {'foo': 'bar'}
    return render(request, 'trading_strategy.html', context)   
# def chart(request):
#     plt.plot(range(10))
#     fig=plt.gcf()
#     buf=io.BytesIO()
#     fig.savefig(buf,format="png")
#     buf.seek(0)
#     string=base64.b64encode(buf.read())
#     uri=urllib.parse.quote(string)
#     return render(request, 'chart.html', {"data":uri})   