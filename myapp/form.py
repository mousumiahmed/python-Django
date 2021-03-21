from django import forms  
from myapp.models import Student  
  
class StuForm(forms.ModelForm):  
    class Meta:  
        model = Student  
        fields = "__all__"

#file upload
class StudentForm(forms.Form):  
    firstname = forms.CharField(label="Enter first name",max_length=50)  
    lastname  = forms.CharField(label="Enter last name", max_length = 10)  
    email     = forms.EmailField(label="Enter Email")  
    file      = forms.FileField() # for creating file input