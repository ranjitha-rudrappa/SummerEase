# text_checker/forms.py

from django import forms


class TextCheckForm(forms.Form):
    input_text = forms.CharField(widget=forms.Textarea)
