# myapp/models.py

from djongo import models

class User(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True, default='default_username')
    password = models.CharField(max_length=100)
    reset_password_token = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self):
        return self.username
