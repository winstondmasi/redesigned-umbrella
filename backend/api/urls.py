# This will handle URL routing specific to our API

from django.urls import path
from .views import analyze_article
from . import views

urlpatterns = [
    path('', views.home, name = 'index'),
    path('analyze_article/', analyze_article, name='analyze_article'),
]