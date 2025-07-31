from django.contrib.auth.models import AbstractUser
from django.db import models
from django.apps import apps
# from academics.models import AcademicYear 

class User(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('lecturer', 'Lecturer'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    admission_number = models.CharField(max_length=30, unique=True)
    # Use string model reference to avoid circular import
    program = models.ForeignKey('academics.Program', on_delete=models.CASCADE, null=True, blank=True)
    semester = models.ForeignKey('academics.Semester', on_delete=models.CASCADE, null=True, blank=True)
    admission_year = models.ForeignKey('academics.AcademicYear', on_delete=models.CASCADE, null=True, blank=True)



    def __str__(self):
        return self.user.username
    
    @property
    def year_of_study(self):
        try:
            current_year = apps.get_model('academics', 'AcademicYear').objects.get(is_current=True)
            admission_year = int(self.admission_year.name.split('/')[0])
            current_year_val = int(current_year.name.split('/')[0])
            return (current_year_val - admission_year) + 1
        except Exception:
            return None

class LecturerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    staff_id = models.CharField(max_length=30, unique=True)
    department = models.CharField(max_length=100)
    def __str__(self):
        return self.user.username
    