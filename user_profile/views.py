from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# its returning the user profile 
@login_required # this is the decorator it adds more functionality like to view this page user must be logged in
def profile(request):
    return render(request,'user_profile/profile.html')