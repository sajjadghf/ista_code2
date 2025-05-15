from django.urls import path
from . import views

urlpatterns = [
    path('getmembers/', views.members),
]
