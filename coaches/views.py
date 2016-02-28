from django.shortcuts import render
from django.http import HttpResponse
from coaches.models import Coach


def detail(request, id_of_coach):
    defined_coach = Coach.objects.get(id = id_of_coach)
#   list_of_lessons = Lesson.objects.filter(course = id_of_course)
    return render(request, 'coaches/detail.html', {'defined_coach' : defined_coach})