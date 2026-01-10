from .models import StudentAnswer

def has_taken_exam(student, exam):
    return StudentAnswer.objects.filter(
        student=student,
        exam=exam
    ).exists()

