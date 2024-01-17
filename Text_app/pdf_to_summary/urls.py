# myapp/urls.py

from django.urls import path
from .views import summarize,texttospeech1,translate_summary1

urlpatterns = [
    path('summarize/', summarize, name='summarize'),
    path('texttospeech1', texttospeech1, name='texttospeech1'),
    path('translate-summary1/', translate_summary1, name='translate_summary1'),
    # Add other paths if needed
]
