# summarization/models.py

from django.db import models


class TextSummarization(models.Model):
    input_text = models.TextField()
    generated_summary = models.TextField(blank=True, null=True)
    translated_summary = models.TextField(blank=True, null=True)
