from django.shortcuts import render
from .models import Product
def input(request):
    return render(request,'input.html')
def insert(request):
    Pid1=int(request.GET['t1']),
    Pname1=request.GET['t2'],
    Pcost=float(request.GET['t3']),
    Pmfd=request.GET['t4']
    Pexpdt=request.GET['t5']
    f=Product(Pid=Pid1,Pname=Pname1,Pcost=Pcost1,Pmfd=Pmfd1,Pexpdt=Pexpdt1)
    f.save()
    return render(request,'links.html')
def display(request):
    recs=Product.objects.all()
    return render(request,'display.html',{'records':recs})


# Create your views here.
