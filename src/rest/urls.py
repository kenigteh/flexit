from django.urls import path

from rest import views

urlpatterns = [
    path('bonus/', views.BonusManager.as_view()),
    path('user_manager/', views.UserManager.as_view()),
]