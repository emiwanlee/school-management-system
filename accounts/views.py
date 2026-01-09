from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from exams.models import Exam
# Create your views here.
@login_required
def student_dashboard(request):
    if request.user.role != 'student':
        return HttpResponseForbidden("Students only")

    exams = Exam.objects.filter(
        school_class=request.user.school_class
    )

    return render(request, 'accounts/student_dashboard.html', {
        'exams': exams
    })