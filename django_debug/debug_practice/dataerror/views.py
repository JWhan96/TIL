from django.shortcuts import render
from .models import TestModel

def data(request):
    test = TestModel.objects.all()
    context = {
        "ab" : test
    }
    return render(request, "dataerror/data.html", context)


def data2(request, pk):
    test = TestModel.objects.get(pk=pk)
    context = {
        "information" : test
    }
    return render(request, "dataerror/data_2.html", context)


def data3(request, pk):
    test = TestModel.objects.get(pk=pk)
    context = {
        'page' : test, 
    }
    return render(request, "dataerror/data_3.html", context)