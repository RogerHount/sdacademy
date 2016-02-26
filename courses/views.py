from django.shortcuts import render
from django.http import HttpResponse
from courses.models import Course, Lesson

def courses_list(request):
	all_courses = Course.objects.all()
	return render(request, 'index.html', {'all_courses' : all_courses})

def detail(request, id_of_course):
	defined_course = Course.objects.get(id = id_of_course)
	list_of_lessons = Lesson.objects.filter(course = id_of_course)
	return render(request, 'courses/detail.html', {'defined_course' : defined_course, 'list_of_lessons' : list_of_lessons})