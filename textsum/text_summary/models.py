# summarizer_app/models.py
from django.db import models


class UserInput(models.Model):
    input_text = models.TextField()
    summary = models.TextField()

    def __str__(self):
        return f"TextSummary #{self.pk}"
