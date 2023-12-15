# models.py
from django.db import models

class PdfDocument(models.Model):
    pdf_file = models.FileField(upload_to='pdfs/')
    pages_to_summarize = models.CharField(max_length=255)
    summarized_text = models.TextField(null=True, blank=True)
