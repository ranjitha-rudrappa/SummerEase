from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class TextSummary(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    input_text = models.TextField()
    generated_summary = models.TextField()

    def __str__(self):
        return f'Summary for {self.user.username}'
