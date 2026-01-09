from django.db import models
from accounts.models import User

class Exam(models.Model):
    title = models.CharField(max_length=100)
    subject = models.ForeignKey(
        'academics.Subject',
        on_delete=models.CASCADE
    )
    school_class = models.ForeignKey(
        'academics.SchoolClass',
        on_delete=models.CASCADE
    )
    total_questions = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class Question(models.Model):
    subject = models.ForeignKey(
        'academics.Subject',
        on_delete=models.CASCADE
    )
    text = models.TextField()

    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)

    correct_option = models.CharField(
        max_length=1,
        choices=(
            ('A', 'Option A'),
            ('B', 'Option B'),
            ('C', 'Option C'),
            ('D', 'Option D'),
        )
    )

    def __str__(self):
        return self.text[:50]


class StudentAnswer(models.Model):
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    exam = models.ForeignKey(
        Exam,
        on_delete=models.CASCADE
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE
    )
    selected_option = models.CharField(max_length=1)
    is_correct = models.BooleanField()
