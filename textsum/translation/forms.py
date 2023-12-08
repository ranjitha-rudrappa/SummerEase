# summarization/forms.py

from django import forms


class SummarizationForm(forms.Form):
    input_text = forms.CharField(widget=forms.Textarea)
    language_choices = [('en', 'English'), ('es', 'Spanish'), ('fr', 'French'),('kn','Kannada'),('te','Telugu'),('hi','Hindi')]  # Add more language choices
    translation_language = forms.ChoiceField(choices=language_choices, label='Select Language for Translation',
                                             required=False)
