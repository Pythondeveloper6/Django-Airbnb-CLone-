from django import forms
from . models import PropertyBook



class PropertyBookForm(forms.ModelForm):
    class Meta:
        model = PropertyBook
        fields = ['name','email','date_from','date_to','guest','children']