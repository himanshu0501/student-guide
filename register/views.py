from django.shortcuts import render, redirect
from .forms import RegisterationForm
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.


def register_student(request):
    form = RegisterationForm()
    if request.method == 'POST':
        form = RegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'successful registered!')
            return HttpResponseRedirect('/home')
        else:
            messages.error(request,'you entered wrong details')
            return HttpResponseRedirect('/home/register')
    context = {'form':form}
    return render(request,'register/register.html',context)
