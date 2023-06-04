from django.http import HttpResponse
from django.shortcuts import render

def inicio(request):
    return render(request, 'index.html')

def resumen20(request):
    return render(request, 'data20.html')

def resumen21(request):
    return render(request, 'data21.html')

def resumen22(request):
    return render(request, 'data22.html')
