from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Detail

def detail(request):
    details=Detail.objects.all()
    return render(request,'home/details.html',{'details':details})
