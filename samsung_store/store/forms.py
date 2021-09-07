from django import forms

class Purchasing(forms.Form):
    card_number = forms.IntegerField()
    csv = forms.IntegerField(max_value='3')
    exp_date = forms.DateField()
    email = forms.EmailField()
    password = forms.PasswordInput()
    