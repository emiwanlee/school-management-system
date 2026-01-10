from django.urls import path
from .views import take_exam

urlpatterns = [
    path('take/<int:exam_id>/', take_exam, name='take_exam'),
]