from django import forms
from .models import product

class Productform(forms.ModelForm):
    model = product
    class Meta:
        model = product
        fields = "__all__"