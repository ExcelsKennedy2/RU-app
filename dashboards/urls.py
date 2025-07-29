from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.student_dashboard, name='student_dashboard'),
    path('lecturer/', views.lecturer_dashboard, name='lecturer_dashboard'),
]
