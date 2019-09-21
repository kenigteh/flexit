from django.urls import path

from rest import views

urlpatterns = [
    path('bonus/', views.BonusManager.as_view()),
]