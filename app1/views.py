from django.shortcuts import render

# Create your views here.
def a1_first(request):
    d={'a':233,'b':43345}
    return render(request,'a1_first.html',d)
def a1_second(request):
    d={'a':245,'b':23,'c':43}
    return render(request,'a1_second.html',d)
    