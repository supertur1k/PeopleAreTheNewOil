from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return render(request, 'login.html')

def master(request):
    return render(request, 'master.html')

def slave(request):
    return render(request, 'slave.html')
