from django import forms
from .models import Books

# book form class defined here
class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'author', 'description', 'publication_year']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'w-full p-2 border rounded',
                    'placeholder': 'Write Book Title...',
                }
            ),
            'author': forms.TextInput(
                attrs={
                    'class': 'w-full p-2 border rounded',
                    'placeholder': 'Write Book Author...',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'w-full p-2 border rounded',
                    'placeholder': 'Write Book description...',
                    'rows': 5,
                }
            ),
             'publication_year': forms.NumberInput(
                attrs={
                    'class': 'w-full p-2 border rounded',
                    'placeholder': 'Write Publication Year...',
                }
            ),
        }
