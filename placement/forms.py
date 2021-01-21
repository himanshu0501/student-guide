# there are two ways in django to make forms 
# 1 is we can use the usercreation form inbuilt given to us by django 
# 2 is we can make our own form in forms.py we can import forms and modelform provided by the django 
# and we can define the attribute of the forms in a class and can add many more details to the form using the meta class
# example of second type of form is given below.

# {
# from django import forms
# from .models import Registeration
# class RegisterationForm(forms.ModelForm):
#     class Meta:
#         model = Registeration
#         fields = ('name','roll_no','batch','address','city','state','phone_no1','phone_no2','hostel','roomno')

#         widgets = {
#             'name':forms.TextInput(attrs={'class':'form-control mb--4','placeholder':'Enter Name'}),
#             'roll_no':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Roll No'}),
#             'batch':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Batch'}),
#             'address':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter Address'}),
#             'city':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter City'}),
#             'state':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter State'}),
#             'phone_no1':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Phone Number 1'}),
#             'phone_no2':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Phone Number 2'}),
#             'hostel':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Hostel'}),
#             'roomno':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Room Number'}),

#         }

# here we are using the first method we will add the attribute to the by default form we are provided to us in django 
# as the user model in django cannot be changed so will make two models one is user and another is extended user where we will connect both of them with the same user

# and in the widget we can change the form details according to ourself 

from django import forms 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from .models import Extendeduser
# Form fields don't have null or blank arguments. Those are for model fields only. For form fields, you just have required.

# To know more about the fields that we get in django use this link https://www.geeksforgeeks.org/django-model-data-types-and-fields-list/
class UserRegisterForm(UserCreationForm): # Here we are inheriting from usercreationform to our registerform class
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User # when we perform the save then the form is saved in this User model 
        fields = ['username','email','password1','password2'] # the order in  which we write in this list will be the order of fields we will see 

        widgets = {
              'username':forms.TextInput(attrs={'placeholder':'Enter Your Roll Number'}),
              'email':forms.TextInput(attrs={'placeholder':'Enter Your Email'}),
              'password1':forms.TextInput(attrs={'placeholder':'Enter passowrd'}),
              'password2':forms.Textarea(attrs={'placeholder':'Enter password'}),
         }
         

class ExtenededuserForm(forms.ModelForm): # here we are creating another form taking the fields from defined in models.py 
    class Meta:  
        model = Extendeduser
        fields = ['name','birth_date','batch','address','state','city','contact_number','hostel','hostel_room']

        widgets = {
              'name':forms.TextInput(attrs={'placeholder':'Enter Name'}),
              'birth_date':forms.TextInput(attrs={'placeholder':'Enter Birthdate (dd/mm/yyyy)'}),
              'batch':forms.TextInput(attrs={'placeholder':'Enter Batch (2000-30)'}),
              'address':forms.Textarea(attrs={'placeholder':'Enter Address'}),
              'state':forms.TextInput(attrs={'placeholder':'Enter Hometown State'}),
              'city':forms.TextInput(attrs={'placeholder':'Enter Hometown City'}),
              'contact_number':forms.TextInput(attrs={'placeholder':'Enter Contact Number'}),
              'hostel':forms.TextInput(attrs={'placeholder':'If alloted'}),
              'hostel_room':forms.TextInput(attrs={'placeholder':'If alloted'}),
              }