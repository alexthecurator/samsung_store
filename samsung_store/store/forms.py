from django import forms
from crispy_forms.helper import FormHelper

class Purchase(forms.Form):
    card = forms.IntegerField(widget=forms.NumberInput)
    csv = forms.IntegerField(widget=forms.NumberInput)
    exp = forms.DateField(widget=forms.DateInput)
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)
    
    def __init__(self, *args, **kwargs):
        super(Purchase, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.fields['csv'].required = False
        
    card.widget.attrs.update({'aria-label': 'card','aria-describedby':'basic-addon2'})
    csv.widget.attrs.update({'aria-label': 'Csv','aria-describedby':'basic-addon2'})
    exp.widget.attrs.update({'aria-label': 'exp','aria-describedby':'basic-addon2'})
    email.widget.attrs.update({'aria-label': 'email','aria-describedby':'basic-addon2'})
    password.widget.attrs.update({'aria-label': 'password','aria-describedby':'basic-addon2'})
