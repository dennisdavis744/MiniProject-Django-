from django import forms
from .models import *

class customer_form(forms.ModelForm):
    class Meta:
        model = customer_registeration

        fields = ('firstname','lastname','age','phone','address','email','location','username','password','confirm_password')
        
        widgets = {
            'firstname':forms.TextInput(attrs={'class':'form-control'}),
            'lastname':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'location':forms.TextInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'}),
            'confirm_password':forms.TextInput(attrs={'class':'form-control'}),
        }

class product_form(forms.ModelForm):
    class Meta:
        model = productsinfo

        fields = ('product_name','price','material','category','image')

        widgets = {
            'product_name':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'material':forms.TextInput(attrs={'class':'form-control'}),
            'category':forms.TextInput(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'}),
        }

class staff_form(forms.ModelForm):
    class Meta:
        model = staff_regsinfo

        fields = ('firstname','lastname','age','email','username','password','confirm_password')
        
        widgets = {
            'firstname':forms.TextInput(attrs={'class':'form-control'}),
            'lastname':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'}),
            'confirm_password':forms.TextInput(attrs={'class':'form-control'}),
        }
        exclude=['verfiystatus']
class addproduct_form(forms.ModelForm):
    class Meta:
        model = addproduct

        fields = ('itemname','itemimage','price','material','category')

        widgets = {
            'itemname':forms.TextInput(attrs={'class':'form-control'}),
            'itemimage':forms.FileInput(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'material':forms.TextInput(attrs={'class':'form-control'}),
            'category':forms.TextInput(attrs={'class':'form-control'}),
        }