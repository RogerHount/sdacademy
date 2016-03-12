from django.shortcuts import render, redirect
from django.http import HttpResponse
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages

def courses_list(request):
	all_courses = Course.objects.all()
	return render(request, 'index.html', {'all_courses' : all_courses})

def detail(request, id_of_course):
	defined_course = Course.objects.get(id = id_of_course)
	list_of_lessons = Lesson.objects.filter(course = id_of_course)
	return render(request, 'courses/detail.html', {'defined_course' : defined_course, 'list_of_lessons' : list_of_lessons})

def add(request):
	if request.method == 'POST':
		form = CourseModelForm(request.POST)
		if form.is_valid():
			course = form.save()
			messages.success(request, "Course %s has been successfully added." % (course.name))
			return redirect('index')
	else:
		form = CourseModelForm()

	return render(request, 'courses/add.html', {'form':form})

def edit(request,id_of_course):
	course = Course.objects.get(id = id_of_course)
	if request.method == 'POST':
		form = CourseModelForm(request.POST, instance = course)
		if form.is_valid():
			course = form.save()
			messages.success(request, "The changes have been saved.")
	else:
		form = CourseModelForm(instance = course)

	return render(request, 'courses/edit.html', {'form':form})


def remove(request,id_of_course):
	course = Course.objects.get(id = id_of_course)
	if request.method == 'POST':
		course.delete()
		messages.success(request, "Course %s has been deleted." % (course.name))
		return redirect('index')

	form = None
	return render(request, 'courses/remove.html', {'form':form})

def add_lesson(request, id_of_course):
	if request.method == 'POST':
		form = LessonModelForm(request.POST)
		if form.is_valid():
			lesson = form.save()
			messages.success(request, "Lesson %s has been successfully added." % (lesson.subject))
			return redirect('courses:detail', id_of_course=id_of_course )
	else:
		form = LessonModelForm(initial = {'course':id_of_course})

	return render(request, 'courses/add_lesson.html', {'form':form})



