from django.forms import ModelForm
from django import forms
from .models import Word

class WordForm(ModelForm):
    class Meta:
        model = Word
        fields = ('foreign_word', 'translation',)
        