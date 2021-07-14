from django.urls import path
from Student.views import universities, students, university_detail, student_detail


urlpatterns = [
    path('', universities),
    path('students/', students),
    path('student_detail/<int:id>/', student_detail),
    path('university_detail/<int:id>/', university_detail),

]