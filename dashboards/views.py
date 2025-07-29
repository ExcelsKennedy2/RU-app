from django.contrib.auth.decorators import login_required
from core.decorators import student_required, lecturer_required
from django.shortcuts import render

@login_required
@student_required
def student_dashboard(request):
    return render(request, 'dashboards/student_dashboard.html')

@login_required
@lecturer_required
def lecturer_dashboard(request):
    return render(request, 'dashboards/lecturer_dashboard.html')
