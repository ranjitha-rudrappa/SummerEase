# summarization/forms.py

from django import forms


class SummarizationForm(forms.Form):
    language_choices = [('en', 'English'), ('es', 'Spanish'), ('fr', 'French'),('kn','Kannada'),('te','Telugu'),('hi','Hindi')]  # Add more language choices
    target_language = forms.ChoiceField(choices=language_choices, label='Select Language for Translation',
                                             required=False)
