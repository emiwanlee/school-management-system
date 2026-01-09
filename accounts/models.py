from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    school_class = models.ForeignKey(
        'academics.SchoolClass',   # 👈 STRING reference
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
