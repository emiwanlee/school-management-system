from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden

from exams.models import Exam, StudentAnswer


@login_required
def student_dashboard(request):
    if request.user.role != 'student':
        return HttpResponseForbidden("Students only")

    exams = Exam.objects.filter(
        school_class=request.user.school_class
    )

    taken_exam_ids = StudentAnswer.objects.filter(
        student=request.user
    ).values_list('exam_id', flat=True)

    return render(request, 'accounts/student_dashboard.html', {
        'exams': exams,
        'taken_exam_ids': taken_exam_ids
    })


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

    def get_success_url(self):
        user = self.request.user

        if user.role == 'student':
            return reverse_lazy('student_dashboard')
        elif user.role == 'teacher':
            return reverse_lazy('teacher_dashboard')
        return reverse_lazy('login')
