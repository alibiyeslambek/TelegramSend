from django import forms

class ApplicationForm(forms.Form):
    phone_number = forms.CharField(max_length=20, label='Phone Number')
    name = forms.CharField(max_length=40, label='Name')
