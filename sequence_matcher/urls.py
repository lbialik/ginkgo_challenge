from django.urls import path
from sequence_matcher import views

urlpatterns = [
    path('', views.sequence_matcher, name='sequence_matcher'),
    path('submit', views.submit, name='submit'),
]