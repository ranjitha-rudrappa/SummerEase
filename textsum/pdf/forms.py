# pdf_summarizer/forms.py

from django import forms


class PdfForm(forms.Form):
    pdf_file = forms.FileField()
    pages_to_summarize = forms.CharField(label='Pages to Summarize (e.g., "1-3, 5, 7")')
