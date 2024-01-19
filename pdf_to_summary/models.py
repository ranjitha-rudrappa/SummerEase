# models.py

from django.db import models

class PdfDocument(models.Model):
    pdf_file = models.FileField(upload_to='pdfs/')
    pages_to_summarize = models.IntegerField()
    summarized_text = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.pdf_file.name} - Pages: {self.pages_to_summarize}"
