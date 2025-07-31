# academics/models.py

from django.db import models
from accounts.models import User, StudentProfile, LecturerProfile

class School(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Program(models.Model):
    name = models.CharField(max_length=150)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class AcademicYear(models.Model):
    name = models.CharField(max_length=20)  # e.g., "2024/2025"
    is_current = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Semester(models.Model):
    SEMESTER_CHOICES = (
        ('1', 'Semester 1'),
        ('2', 'Semester 2'),
    )
    name = models.CharField(max_length=1, choices=SEMESTER_CHOICES)

    def __str__(self):
        return f"Semester {self.name}"

class Course(models.Model):
    code = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    year_of_study = models.IntegerField()
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.code} - {self.title}"

class CourseRegistration(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student.admission_number} - {self.course.code}"

class LecturerCourseAssignment(models.Model):
    lecturer = models.ForeignKey(LecturerProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.lecturer.staff_id} - {self.course.code}"
