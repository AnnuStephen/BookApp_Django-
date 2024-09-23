

from django import forms
from .models import Book,Author


#  modelform -- make form validation easy

class AuthorForm(forms.ModelForm):
    #  pass additional informations in forms
    class Meta:
        model = Author
        fields = ['name']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'   # __all__ is for fetch all fields from the model

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter the book name'}),
            'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Enter the book author'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the price'})

        }



