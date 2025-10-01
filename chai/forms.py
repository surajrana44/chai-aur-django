from django import forms
from .models import chaiVariety

class ChaiVarietyForm(forms.Form):
   chai_variety = forms.ModelChoiceField(queryset=chaiVariety.objects.all(), label="select chai variety")   
    

