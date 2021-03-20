from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime
from django.http import HttpResponse, HttpResponseNotFound

def hello(request):
    return HttpResponse("<h2>Hellow Welcome Django !</h2>")

def index(request):  
    now = datetime.datetime.now()  
    html = "<html><body><h3>Now time is %s.</h3></body></html>" % now  
    return HttpResponse(html)    # rendering the template in HttpResponse 
