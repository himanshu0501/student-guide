from django import forms

class RegisterForm(forms.Form):
    Name = forms.CharField()
    RollNo = forms.IntegerField()
    FatherName = forms.CharField()
    MobileNo = forms.CharField(max_length=15)
    Emailid = forms.CharField(max_length=50)
    Address = forms.CharField(widget=forms.Textarea)

    
