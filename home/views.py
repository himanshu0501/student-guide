from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

def detail(request):
    return render(request,'home/details.html')

def events(request):
    return render(request,'home/events.html')
