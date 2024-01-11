from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse
def create_student(request):
    ESFO=StudentForm()
    d={'ESFO':ESFO}
    if request.method=='POST':
        SDFO=StudentForm(request.POST)
        if SDFO.is_valid():
            SDFO.save()
            return HttpResponse('create_student done')
        else:
            return HttpResponse('invalid')
    
    return render(request,'create_student.html',d)


