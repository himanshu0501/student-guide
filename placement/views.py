from django.shortcuts import render , redirect
from .forms import UserRegisterForm , ExtenededuserForm# this is the form that we have created in the forms.py file using the usercreation form
from django.contrib import messages # we are importing it to show the flash messages.
from django.contrib.auth.decorators import login_required
# different type of messages that this library have
# message.debug
# message.info
# message.error
# message.success
# message.warning
# django already have some forms which is used as user creation form
# these forms are classes which will be converted into html later

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) # if form is having some data then we are retrieving that data using the POST request "which we say bound state of the form"
        user_detailform = ExtenededuserForm(request.POST)
        if form.is_valid() and user_detailform.is_valid(): # here we are checking is our form is valid  or not  
            user = form.save()
            user_details = user_detailform.save(commit=False) # it will create a userdetail object but won't save it and give it to us.
            user_details.user=user
            user_details.save()
            username = form.cleaned_data.get('username') # here we are retrieving the username from the form that input the data #Any data the user submits through a form will be passed to the server as strings. It doesn't matter which type of form field was used to create the form. Eventually, the browser would will everything as strings. When Django cleans the data it automatically converts data to the appropriate type. For example IntegerField data would be converted to an integer, CharField data would be converted to a string, BooleanField data would be converted to a bool i.e True or False and so on. In Django, this cleaned and validated data is commonly known as cleaned data. We can access cleaned data via cleaned_data dictionary:
            messages.success(request,f'Account created for {username},Now you can login!')
            return redirect('login')
    else: #You must never access the data directly using self.field_name as it may not be safe.
        user_detailform = ExtenededuserForm()
        form = UserRegisterForm() # this is the unbound state when form is empty shown at first time and data is there to retrieve from it.
    return render(request,'placement/registeration.html',{'user_detailform':user_detailform,'form':form})


 # this function is returing the base view of the placement app
def home(request):
    return render(request,'placement/home.html')

# its returning the user profile 
@login_required # this is the decorator it adds more functionality like to view this page user must be logged in
def profile(request):
    return render(request,'placement/profile.html')