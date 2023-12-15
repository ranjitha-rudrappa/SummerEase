# urls.py
from django.urls import path
from .views import register, user_login, feedback, activity_history

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('feedback/', feedback, name='feedback'),
    path('activity_history/', activity_history, name='activity_history'),
]
