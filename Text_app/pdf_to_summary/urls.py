# myapp/urls.py

from django.urls import path
from .views import summarize

urlpatterns = [
    path('summarize/', summarize, name='summarize'),
    # Add other paths if needed
]
