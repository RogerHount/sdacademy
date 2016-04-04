# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.http import HttpResponse
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


def courses_list(request):
	all_courses = Course.objects.all()
	return render(request, 'index.html', {'all_courses' : all_courses})

class CourseDetailView(DetailView):
	model = Course
	template_name= 'courses/detail.html'

	def get_context_data(self, **kwargs):
		context = super(CourseDetailView, self).get_context_data(**kwargs)
		defined_course = super(CourseDetailView, self).get_object()
		list_of_lessons = Lesson.objects.filter(course = defined_course.id)
		context['defined_course'] = defined_course
		context['list_of_lessons'] = list_of_lessons
		return context


class CourseCreateView(CreateView):
	model = Course
	template_name= 'courses/add.html'

	def get_context_data(self, **kwargs):
		context = super(CourseCreateView, self).get_context_data(**kwargs)
		context['title'] = "Course creation"
		return context

	def form_valid(self, form):
		course = form.save()
		messages.success(self.request, "Course %s has been successfully added." % (course.name))
		return super(CourseCreateView, self).form_valid(form)




class CourseUpdateView(UpdateView):
	model = Course
	template_name= 'courses/edit.html'

	def get_context_data(self, **kwargs):
		context = super(CourseUpdateView, self).get_context_data(**kwargs)
		context['buttonname'] = "Изменить"
		context['title'] = "Course update"
		return context

	def form_valid(self, form):
		course = form.save()
		messages.success(self.request, "The changes have been saved.")
		return super(CourseUpdateView, self).form_valid(form)

	def get_success_url(self):
		return reverse_lazy('courses:edit', kwargs={ 'pk': self.object.pk, })






class CourseDeleteView(DeleteView):
	model = Course
	template_name = 'courses/remove.html'

	def get_context_data(self, **kwargs):
		context = super(CourseDeleteView, self).get_context_data(**kwargs)
		context['title'] = "Course deletion"
		course = super(CourseDeleteView, self).get_object()
		message_content = "Course %s has been deleted." % (course.name)
		messages.success(self.request, message_content)
		return context

	def form_valid(self, form):
		course = form.save()
		return super(CourseDeleteView, self).form_valid(form)

	def get_success_url(self):
		return reverse_lazy('index')

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



