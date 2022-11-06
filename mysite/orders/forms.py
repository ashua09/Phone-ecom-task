from dataclasses import fields
from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    '''
       Form to save the details of user while placing order.
    '''
    class Meta:
        model = Order
        fields = ['first_name','last_name','phone','email','address_line_1','address_line_2','country','state','city','order_note']

