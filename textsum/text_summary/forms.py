# summarizer_app/forms.py

from django import forms

class SummarizerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
