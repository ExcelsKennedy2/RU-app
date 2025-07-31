from django.contrib import admin
from .models import (
    School,
    Program,
    AcademicYear,
    Semester,
    Course,
    CourseRegistration,
    LecturerCourseAssignment
)

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'school')
    search_fields = ('name',)
    list_filter = ('school',)

@admin.register(AcademicYear)
class AcademicYearAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'title', 'program', 'year_of_study', 'semester')
    search_fields = ('code', 'title')
    list_filter = ('program', 'semester', 'year_of_study')

@admin.register(CourseRegistration)
class CourseRegistrationAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'academic_year')
    search_fields = ('student__admission_number', 'course__code')
    list_filter = ('academic_year', 'course__program')

@admin.register(LecturerCourseAssignment)
class LecturerCourseAssignmentAdmin(admin.ModelAdmin):
    list_display = ('lecturer', 'course', 'academic_year')
    search_fields = ('lecturer__staff_id', 'course__code')
    list_filter = ('academic_year', 'course__program')
