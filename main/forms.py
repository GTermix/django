from django import forms


class RegForm(forms.Form):
    name = forms.CharField(max_length=30,label="Name")
    email = forms.EmailField(label="Email")
    pass1 = forms.CharField(widget=forms.PasswordInput,label="Enter password")
    pass2 = forms.CharField(widget=forms.PasswordInput,label="Re-enter password")
