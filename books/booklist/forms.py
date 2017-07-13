# encoding: utf-8
from django import forms
from .models import BookList
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm 


class RenewBookForm(forms.ModelForm):
    class Meta:
        model = BookList
        fields = ('title', 'text', 'author')

class DeleteBookForm(forms.ModelForm):
    class Meta:
        model = BookList
        fields = ('title', )
        sucess_url = reverse_lazy('title')

class EditBookForm(forms.ModelForm):
    class Meta:
        model = BookList
        fields = ['title', 'text', 'author']

