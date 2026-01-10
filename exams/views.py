from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .utils import has_taken_exam

# Create your views here.
@login_required
def take_exam(request, exam_id):
    if request.user.role != 'student':
        return HttpResponseForbidden("Students only")

    exam = get_object_or_404(Exam, id=exam_id)

    # Ensure exam belongs to student's class
    if exam.school_class != request.user.school_class:
        return HttpResponseForbidden("Not your class exam")

         # 🚫 Prevent retake
    if has_taken_exam(request.user, exam):
        return HttpResponseForbidden("You have already taken this exam")

    questions = Question.objects.filter(
        subject=exam.subject
    )[:exam.total_questions]

    if request.method == 'POST':
        score = 0
        for q in questions:
            selected = request.POST.get(str(q.id))
            is_correct = selected == q.correct_option
            if is_correct:
                score += 1

            StudentAnswer.objects.create(
                student=request.user,
                exam=exam,
                question=q,
                selected_option=selected,
                is_correct=is_correct
            )

        return render(request, 'exams/result.html', {
            'score': score,
            'total': questions.count()
        })

    return render(request, 'exams/take_exam.html', {
        'exam': exam,
        'questions': questions
    })