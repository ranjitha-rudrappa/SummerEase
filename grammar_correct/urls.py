# urls.py
from django.urls import path
from .views import grammar_checker

urlpatterns = [
    path('grammar/', grammar_checker, name='grammar_checker'),
]
