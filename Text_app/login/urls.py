from django.urls import path
from .views import signup, login,home,dashboard,forgot_password

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('dashboard/',dashboard,name='dashboard'),
    path('forgot_password/',forgot_password,name='forgot_password')
    # Add other URLs as needed
]
