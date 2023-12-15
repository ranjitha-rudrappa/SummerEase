from django.db import models
import os

def get_upload_path(instance, filename):
    return os.path.join('pdfs', filename)

class PdfDocument(models.Model):
    pdf_file = models.FileField(upload_to=get_upload_path)
    pages_to_summarize = models.CharField(max_length=255)
    summarized_text = models.TextField(null=True, blank=True)
