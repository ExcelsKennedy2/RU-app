# core/decorators.py
from django.core.exceptions import PermissionDenied

def student_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.role != 'student':
            raise PermissionDenied
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def lecturer_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.role != 'lecturer':
            raise PermissionDenied
        return view_func(request, *args, **kwargs)
    return _wrapped_view
