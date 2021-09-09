from django import forms
from crispy_forms.helper import FormHelper

class Purchase(forms.Form):
    card = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control', 'maxlength': '12'}), initial='', required=False)
    csv = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control', 'maxlength': '3'}), initial='', required=False)
    exp = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'type': 'date'}), initial='', required=False)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}), initial='', required=False)
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':"Account password", 
                'autocomplete':'password', 
                'aria-label':"Account password", 
                'aria-describedby':"basic-addon2",
                'maxlength': '16'
            }
        ), initial='', label='', required=False
    )
    
    def __init__(self, *args, **kwargs):
        super(Purchase, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.fields['exp'].type = 'date'
        
