from django.shortcuts import render

# Create your views here.
def a2_first(request):
    d={'a':112 ,'b':32,'c':23}
    return render(request,'a2_first.html',d)
def a2_second(request):
    d={'a':'NAGARJUNA'}
    return render(request,'a2_second.html',d)