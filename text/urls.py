from django.contrib import admin
from django.urls import path,include
from django.contrib import admin
from django.urls import path
from . import views
from .views import translate_summary

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index,name='index'),
    path('output', views.output,name='output'),
    path('texttospeech',views.texttospeech,name='texttospeech'),
    path('translate-summary/', translate_summary, name='translate_summary'),
    
]