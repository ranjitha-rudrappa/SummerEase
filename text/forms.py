# forms.py

from django import forms

class SummarizationForm(forms.Form):
    target_language_choices = [
        ('en', 'English'),
        ('es', 'Spanish'),
        ('fr', 'French'),
        ('kn', 'Kannada'),
        ('te', 'Telugu'),
        ('hi', 'Hindi')
    ]
    target_language = forms.ChoiceField(choices=target_language_choices, label='Select Target Language', required=True)
