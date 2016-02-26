from django.shortcuts import render
from django.http import HttpResponse
from students.models import Student
from courses.models import Course, Lesson


def list_view(request):
	course_owner = request.GET.get('course_id', '')
	
	if course_owner:
		all_students = Student.objects.filter(courses = course_owner)
		return render(request, 'students/list.html', {'all_students' : all_students, 'course_owner' : course_owner })
	else:
		all_students = Student.objects.all()
		return render(request, 'students/list.html', {'all_students' : all_students })

def detail(request, id_of_student):
	the_student = Student.objects.get(id = id_of_student)
	return render(request, 'students/detail.html', {'the_student': the_student })
