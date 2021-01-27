from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from placement.forms import UserUpdateForm,ProfileUpdateForm
from django.contrib import messages

# its returning the user profile 
@login_required # this is the decorator it adds more functionality like to view this page user must be logged in
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user) # instance= request.user will show the current user detail already filled in
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile) #instance= request.user.profile will show the current user profile image filled # request.FILES will show the current user file that it have
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your account have been successfully updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user) # instance= request.user will show the current user detail already filled in
        p_form = ProfileUpdateForm(instance=request.user.profile) #instance= request.user.profile will show the current user profile image filled
    context = {
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request,'user_profile/profile.html',context)