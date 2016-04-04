from django.shortcuts import render
from django.http import HttpResponse
from coaches.models import Coach
from courses.models import Course

def detail(request, id_of_coach):
    defined_coach = Coach.objects.get(id = id_of_coach)
    defined_course_coach = Course.objects.filter(coach = id_of_coach)
    defined_course_assistant = Course.objects.filter(assistant = id_of_coach)

    return render(request, 'coaches/detail.html', {'defined_coach' : defined_coach, 'defined_course_coach' : defined_course_coach, 'defined_course_assistant' : defined_course_assistant})