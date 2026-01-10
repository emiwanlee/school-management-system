from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from exams.models import Exam, StudentAnswer

# Create your views here.
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
        'take_exam_ids': take_exam_ids
    })