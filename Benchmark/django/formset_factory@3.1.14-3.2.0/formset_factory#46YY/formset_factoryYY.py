from django import forms

class ExampleForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
from django.forms import formset_factory
ExampleFormSet = formset_factory(ExampleForm,  ExampleForm,  1,  False,  False,  None,  False,  None, validate_min=False)
