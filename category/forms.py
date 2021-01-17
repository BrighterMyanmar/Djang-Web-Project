from django import forms 
from .models import SubCategory

class SubCatFrom(forms.ModelForm):
    class Meta :
        model = SubCategory
        fields = '__all__'
        labels = {
            'name':'Category Name',
            'parent':"Parent Name"
        }

    def __init__(self,*args,**kwargs):
        super(SubCatFrom,self).__init__(*args,**kwargs)
        self.fields['parent'].empty_label = 'Select'
        # self.fields['name'].required = False
