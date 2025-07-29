from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home, name='home'),
    path('register/student/', views.student_register, name='student_register'),
    path('register/lecturer/', views.lecturer_register, name='lecturer_register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('redirect/', views.role_redirect_view, name='role_redirect'),
]