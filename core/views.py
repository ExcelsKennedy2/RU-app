from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'home.html')

from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from .forms import StudentRegisterForm, LecturerRegisterForm

# Registration Views
def student_register(request):
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = StudentRegisterForm()
    return render(request, 'student_register.html', {'form': form})

def lecturer_register(request):
    if request.method == 'POST':
        form = LecturerRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = LecturerRegisterForm()
    return render(request, 'lecturer_register.html', {'form': form})

# Role-based redirection after login
@login_required
def role_redirect_view(request):
    if request.user.role == 'student':
        return redirect('student_dashboard')
    elif request.user.role == 'lecturer':
        return redirect('lecturer_dashboard')
    else:
        return redirect('admin:index')
