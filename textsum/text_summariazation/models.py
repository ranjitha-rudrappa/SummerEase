# text_generation/models.py

from django.db import models


class TextGeneration(models.Model):
    user_input = models.TextField()
    generated_output = models.TextField()

