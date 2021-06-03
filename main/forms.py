from .models import Orders
from django.forms import ModelForm, TextInput, Textarea
    

class OrderForm(ModelForm):
    
    class Meta:
        model = Orders
        fields = ['first_name', 'Middle_name', 'Phone', 'Address', 'Cart']

        widgets = {
            'first_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            'Middle_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Отчество'
            }),
            'Phone': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер телефона'
            }),
            'Address': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес'
            }),
            'Cart': Textarea(attrs={
                'id': 'CartList',
                'class': 'form-control d-none',
                'rows': '3',
                
            })
        }