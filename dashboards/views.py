from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def student_dashboard(request):
    return render(request, 'dashboards/student_dashboard.html')

@login_required
def lecturer_dashboard(request):
    return render(request, 'dashboards/lecturer_dashboard.html')
