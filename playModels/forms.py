from django import forms
from .models import Users

class MyForm(forms.ModelForm):
    class meta :
        User=Users
        fields=["first_name","last_name","ph_number"]
        labels={"first_name":"First Name","last_name":"Last Name","ph_number":"Phone Number"}