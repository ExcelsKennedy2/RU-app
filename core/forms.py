from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User, StudentProfile, LecturerProfile
from academics.models import Program, Semester 

class StudentRegisterForm(UserCreationForm):
    admission_number = forms.CharField()
    program = forms.ModelChoiceField(queryset=Program.objects.all())
    semester = forms.ModelChoiceField(queryset=Semester.objects.all())

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'student'
        if commit:
            user.save()
            StudentProfile.objects.create(
                user=user,
                admission_number=self.cleaned_data['admission_number'],
                program=self.cleaned_data['program'],
                semester=self.cleaned_data['semester'],
            )
        return user

class LecturerRegisterForm(UserCreationForm):
    staff_id = forms.CharField()
    department = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'lecturer'
        if commit:
            user.save()
            LecturerProfile.objects.create(
                user=user,
                staff_id=self.cleaned_data['staff_id'],
                department=self.cleaned_data['department']
            )
        return user
