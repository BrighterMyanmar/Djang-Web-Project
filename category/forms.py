from django import forms 
from .models import SubCategory

class SubCatFrom(forms.ModelForm):
    class Meta :
        model = SubCategory
        fields = '__all__'