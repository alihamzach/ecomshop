from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import ReviewRating, CustomUser


class ReviewObject(forms.ModelForm):
    class Meta:
        model = ReviewRating
        fields = ['name', 'title', 'review']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'review': forms.Textarea(attrs={'class': 'form-control'}),
        }


class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username']


class CartForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['myuser', 'first_name', 'last_name', 'company_name', 'area_code', 'primary_phone', 'street_address',
                  'zip_code', 'busniess_address']


class CartPaymentForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['cardholder_name', 'card_Number', 'month', 'year', 'csd']
