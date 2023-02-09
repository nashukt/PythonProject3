from django.http import HttpResponse
from django.shortcuts import render
from .models import place
from .models import TeamMember


# Create your views here.

def demo(request):
    obj = place.objects.all()
    obj1 = TeamMember.objects.all()
    return render(request, 'index.html', {'result': obj, 'result1': obj1})
# def expression(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     sum=x+y
#     sub=x-y
#     mul=x*y
#     div=x/y
#     return render(request,"result.html",{'result':sum,'result1':sub,'result2':mul,'result3':div})
