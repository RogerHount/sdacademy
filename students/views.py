from django.shortcuts import render, redirect
from django.http import HttpResponse
from students.models import Student
from courses.models import Course, Lesson
from students.forms import StudentModelForm
from django.contrib import messages

def list_view(request):
	course_owner = request.GET.get('course_id', '')
	
	if course_owner:
		all_students = Student.objects.filter(courses = course_owner)
		return render(request, 'students/list.html', {'all_students' : all_students, 'course_owner' : course_owner })
	else:
		all_students = Student.objects.all()
		return render(request, 'students/list.html', {'all_students' : all_students })

def detail(request, id_of_student):
	the_student = Student.objects.get(pk = id_of_student)
	return render(request, 'students/detail.html', {'the_student': the_student })

def create(request):
	context = {}
	if request.method == 'POST':
		form = StudentModelForm(request.POST)
		if form.is_valid():
			student = form.save()
			messages.success(request, "Student %s %s has been successfully added." % (student.name, student.surname))
			return redirect('students:list_view')
			
	else:
		form = StudentModelForm()

	return render(request, 'students/add.html', {'form':form})

def edit(request, student_to_edit):
	student = Student.objects.get(pk = student_to_edit)
	if request.method == 'POST':
		form = StudentModelForm(request.POST, instance = student)
		if form.is_valid():
			student = form.save()
			messages.success(request, "Info on the student has been sucessfully changed.")
			
	else:
		form = StudentModelForm(instance = student)
	return render(request, 'students/edit.html', {'form':form})


def remove(request, student_to_remove):
	student = Student.objects.get(pk = student_to_remove)
	if request.method == 'POST':
		student.delete()
		messages.success(request, "Info on %s %s has been sucessfully deleted." % (student.name, student.surname))
		return redirect('students:list_view')
	form = None
	return render(request, 'students/remove.html', {'form':form})