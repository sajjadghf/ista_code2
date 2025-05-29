from django.urls import path
from . import views

urlpatterns = [
    path('getstudents', views.ListStudents.as_view()),
    path('getstudents_v2', views.list_stu),
    path('getstudents_v3/<int:pk>/', views.CRUD_Students.as_view()),
    path('getmembers/', views.members),
    path('getinfo/<str:sname>', views.info),]
