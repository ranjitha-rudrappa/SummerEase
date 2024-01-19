from django.db import models
from django.contrib.auth.models import User

class Summary(models.Model):
    input_text = models.TextField()
    generated_summary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return f'Summary #{self.id} - {self.created_at}'
