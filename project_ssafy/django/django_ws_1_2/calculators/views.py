from django.shortcuts import render

# Create your views here.
def calculators(request):
    
    return render(request, 'calculators/calculators.html')

def results(request):
    
    return render(request, 'calculators/results.html')