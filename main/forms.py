from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *


class NewCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(NewCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = "__all__"


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
