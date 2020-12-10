from django.shortcuts import render
from .models import clubs as clubss
# Create your views here.
def clubs(request):
    club=clubss.objects.all()
    return render(request,'home/clubs.html',{'club':club})