# -*- coding: utf-8 -*-
from django.shortcuts import render
import math


def quadratic_results(request):
	error_count = 0
	a = request.GET.get('a', '')
	b = request.GET.get('b', '')
	c = request.GET.get('c', '')
	a_error_code = ''
	b_error_code = ''
	c_error_code = ''
	answer = ''
	x1 = 0
	x2 = 0

	# a checks
	if not a:
		error_count = error_count + 1
		a_error_code = "коэффициент не определен"
	elif not a.replace('-', '').isdigit():
		error_count = error_count + 1
		a_error_code = "коэффициент не целое число"	

	elif int(a) == 0:
		error_count = error_count + 1
		a_error_code = "коэффициент при первом слагаемом уравнения не может быть равным нулю"

	# b checks
	if not b:
		error_count = error_count + 1
		b_error_code = "коэффициент не определен"
	elif not b.replace('-', '').isdigit():
		error_count = error_count + 1
		b_error_code = "коэффициент не целое число"	

	
	# c checks
	if not c:
		error_count = error_count + 1
		c_error_code = "коэффициент не определен"
	elif not c.replace('-', '').isdigit():
		error_count = error_count + 1
		c_error_code = "коэффициент не целое число"	


	if error_count > 0:	
		return render(request, 'results.html', {'a':a, 'b':b, 'c':c, 'a_error_code':a_error_code, 'b_error_code':b_error_code, 'c_error_code':c_error_code})

	else:
		a = int(a)
		b = int(b)
		c = int(c)

		#Discriminanto
		discr = b * b - 4 * a * c

		if discr < 0:
			discr_answer = "Дискриминант: %r" % (discr)
			answer = "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
			return render(request, 'results.html', {'a':a, 'b':b, 'c':c, 'discr':discr, 'discr_answer':discr_answer, 'answer':answer })
		
		elif discr == 0:
			x1 = (-b) / 2.0 * a
			x2 = x1
			discr_answer = "Дискриминант: %r" % (discr)
			answer = "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %r" % (x1)
			return render(request, 'results.html', {'a':a, 'b':b, 'c':c, 'discr':discr, 'discr_answer':discr_answer, 'answer':answer })
		
		elif discr > 0:
			x1 = ((-b) + math.sqrt(discr)) / (2.0 * a)
			x2 = ((-b) - math.sqrt(discr)) / (2.0 * a)
			discr_answer = "Дискриминант: %r" % (discr)
			answer = "Квадратное уравнение имеет два действительных корня: x1 = %r, x2 = %r" % (round(x1, 1), round(x2, 1))
			return render(request, 'results.html', {'a':a, 'b':b, 'c':c, 'discr':discr, 'discr_answer':discr_answer, 'answer':answer })