from django.shortcuts import render

def detail(request):
    return render(request,'home/details.html')

def events(request):
    return render(request,'home/events.html')
