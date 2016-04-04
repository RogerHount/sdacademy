# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from students.models import Student
from courses.models import Course, Lesson
from students.forms import StudentModelForm
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class StudentListView(ListView):
	model = Student
	paginate_by = 2

	def get_queryset(self):
		queryset = super(StudentListView, self).get_queryset()
		course_id = self.request.GET.get('course_id', '')
		if course_id:
			queryset = Student.objects.filter(courses = course_id)
		return queryset

		
class StudentDetailView(DetailView):
	model = Student
	

class StudentCreateView(CreateView):
	model = Student

	def get_context_data(self, **kwargs):
		context = super(StudentCreateView, self).get_context_data(**kwargs)
		context['buttonname'] = "Создать"
		context['title'] = 'Student registration'
		return context

	def form_valid(self, form):
		student = form.save()
		messages.success(self.request, "Student %s %s has been successfully added." % (student.name, student.surname))
		return redirect('students:list_view')


class StudentUpdateView(UpdateView):
	model = Student
	
	def get_context_data(self, **kwargs):
		context = super(StudentUpdateView, self).get_context_data(**kwargs)
		context['buttonname'] = "Изменить"
		context['title'] = "Student info update"
		return context

	def form_valid(self, form):
		student = form.save()
		messages.success(self.request, "Info on the student has been sucessfully changed.")
		return super(StudentUpdateView, self).form_valid(form)

	def get_success_url(self):
		return reverse_lazy('students:edit', kwargs={ 'pk': self.object.pk, })


class StudentDeleteView(DeleteView):
	model = Student

	def get_context_data(self, **kwargs):
		context = super(StudentDeleteView, self).get_context_data(**kwargs)
		context['buttonname'] = "Удалить"
		context['title'] = "Student info suppression"
		
		return context

	def get_success_url(self):
		studentdetails = super(StudentDeleteView, self).get_object()
		message_content = "Info on %s %s has been sucessfully deleted." % (studentdetails.name, studentdetails.surname)
		messages.success(self.request, message_content)
		return reverse_lazy('students:list_view')

	def form_valid(self, form):
		student = form.save()
		return super(StudentDeleteView, self).form_valid(form)

#SuccessMessageMixin hooks to form_valid which is not present on DeleteView to push its message to the user.
#	def delete(self, request, *args, **kwargs):
#		messages.success(self.request, self.success_message)
#		return super(StudentDeleteView, self).delete(request, *args, **kwargs)
