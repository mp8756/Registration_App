
from django import forms
from home.models import StudentProfile

class CustomuserForms(forms.Form):

    Name = forms.CharField(max_length=200)
    Registration_number = forms.IntegerField()
    Branch = forms.CharField(max_length=30)
    Yearsofstudy = forms.IntegerField()
    Mobile_number = forms.IntegerField()
    Email = forms.CharField(max_length=50)
    Gender = forms.CharField(max_length=20)
    Current_address = forms.CharField(max_length=50)
    Permanent_address = forms.CharField(max_length=50)
    Nationality = forms.CharField(max_length=20)




class StudentProfileForm(forms.ModelForm):

    class Meta:
        model = StudentProfile
        fields = ["name","registration_number", "branch", "yearsofstudy", "mobile_number", "email", "gender"]
