# urls.py
from django.urls import path
from .views import grammar_check

urlpatterns = [
    path('grammar-check/', grammar_check, name='grammar_check'),
]
