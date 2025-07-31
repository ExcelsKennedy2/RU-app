from django.contrib.auth.decorators import login_required
from core.decorators import student_required, lecturer_required
from django.shortcuts import render, redirect
from accounts.models import StudentProfile
from academics.models import AcademicYear, Semester, Course, CourseRegistration


@login_required
@student_required
def student_dashboard(request):
    user = request.user

    try:
        student = StudentProfile.objects.get(user=user)
    except StudentProfile.DoesNotExist:
        return redirect('home')

    # Get current academic year and semester
    try:
        current_year = AcademicYear.objects.get(is_current=True)
        current_semester = Semester.objects.get(is_current=True)
    except (AcademicYear.DoesNotExist, Semester.DoesNotExist):
        current_year = None
        current_semester = None

    year_of_study = student.year_of_study

    available_courses = []
    if current_semester and student.program and year_of_study:
        available_courses = Course.objects.filter(
            program=student.program,
            year_of_study=year_of_study,
            semester=current_semester
        )

    registered_courses = CourseRegistration.objects.filter(
        student=student,
        academic_year=current_year
    ).select_related('course')

    # Allow registration
    if request.method == 'POST':
        course_ids = request.POST.getlist('course_ids')
        for course_id in course_ids:
            course = Course.objects.get(id=course_id)
            CourseRegistration.objects.get_or_create(student=student, course=course, academic_year=current_year)
        return redirect('student_dashboard')

    context = {
        'student': student,
        'current_year': current_year,
        'current_semester': current_semester,
        'available_courses': available_courses,
        'registered_courses': registered_courses,
        'year_of_study': year_of_study,
    }

    return render(request, 'dashboards/student_dashboard.html', context)


@login_required
@lecturer_required
def lecturer_dashboard(request):
    return render(request, 'dashboards/lecturer_dashboard.html')
