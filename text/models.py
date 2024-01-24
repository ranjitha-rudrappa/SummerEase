from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User

class TextSummary(models.Model):
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    input_text = models.TextField()
    generated_summary = models.TextField()

    def __str__(self):
        return f'Summary for {self.user.username}'
