from djongo import models


class PdfDocument(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    pdf_file = models.FileField(upload_to='pdfs/')
    summarized_text = models.TextField()
    pages_to_summarize = models.CharField(max_length=255)
