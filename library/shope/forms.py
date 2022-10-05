
from .models import Book
from django.forms import ModelForm, TextInput, Textarea


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["name","description"]
        widgets ={
            'name': TextInput(attrs={
            'class':'form-control',
            'placeholder':"название"
        }),
            'description': Textarea(attrs={
            'class':'form-control',
            'placeholder':"Описание"
        })
        }