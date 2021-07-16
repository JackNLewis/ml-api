from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from predict import views

urlpatterns = [
    path('predict/cnn', views.Cnn),
]
