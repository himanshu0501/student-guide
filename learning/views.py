from django.shortcuts import render


def welcome(request):
    return render(request,'learning/welcome.html')


