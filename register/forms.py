from django import forms
from .models import Registeration



class RegisterationForm(forms.ModelForm):
    class Meta:
        model = Registeration
        fields = ('name','roll_no','batch','address','city','state','phone_no1','phone_no2','hostel','roomno')

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control mb--4','placeholder':'Enter Name'}),
            'roll_no':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Roll No'}),
            'batch':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Batch'}),
            'address':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter Address'}),
            'city':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter City'}),
            'state':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter State'}),
            'phone_no1':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Phone Number 1'}),
            'phone_no2':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Phone Number 2'}),
            'hostel':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Hostel'}),
            'roomno':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Room Number'}),

        }