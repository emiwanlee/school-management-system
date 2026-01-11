from django.urls import path
from .views import CustomLoginView, student_dashboard

urlpatterns = [
     path('login/', CustomLoginView.as_view(), name='login'),
    path('student/dashboard/', student_dashboard, name='student_dashboard'),
]
