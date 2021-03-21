from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime
from django.http import HttpResponse, HttpResponseNotFound
from django.template import loader
from django.shortcuts import render  
from myapp.form import StuForm
from myapp.form import StudentForm
#from myapp.functions.functions import handle_uploaded_file

def hello(request):
    return HttpResponse("<h2>Hellow Welcome Django !</h2>")

def index(request):  
    now = datetime.datetime.now()  
    html = "<html><body><h3>Now time is %s.</h3></body></html>" % now  
    return HttpResponse(html)    # rendering the template in HttpResponse 

def templ(request):  
   name={"name":"mousumi"}
   template = loader.get_template('index.html') # getting our template  
   return HttpResponse(template.render(name))

def form(request):  
    stu = StuForm()  
    return render(request,"index.html",{'form':stu}) 

def fileupload(request):  
    if request.method == 'POST':  
        student = StudentForm(request.POST, request.FILES)  
        if student.is_valid():  
            handle_uploaded_file(request.FILES['file'])  
            return HttpResponse("File uploaded successfuly")  
    else:  
        student = StudentForm()  
        return render(request,"index.html",{'form1':student})