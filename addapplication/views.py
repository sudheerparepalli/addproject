from django.shortcuts import render
from django.http import HttpResponse
def input(request):
    return render(request,'input.html')
def add(request):
    v1=request.GET["t1"]
    v2=request.GET["t2"]
    try:
        i=int(v1)
        j=int(v2)
        z=i+j
        return HttpResponse(z)
    except(ValueError):
        return render(request,'input.html')
    # Create your views here.
