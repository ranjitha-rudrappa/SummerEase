# forms.py
from django import forms

class PdfForm(forms.Form):
    pdf_file = forms.FileField()
    pages_to_summarize = forms.CharField(max_length=255)
