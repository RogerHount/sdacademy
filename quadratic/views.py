# -*- coding: utf-8 -*-
from django.shortcuts import render
from django import forms
from quadratic.forms import QuadraticForm


def quadratic_results(request):
	context={}
	if request.method == 'GET' and request.GET.keys():
		form = QuadraticForm(request.GET)
		if form.is_valid():
			a = context['a'] = request.GET.get('a','')
			b = context['b'] = request.GET.get('b','')
			c = context['c'] = request.GET.get('c','')

			context['d'] = float(b)**2 - 4*float(a)*float(c)
			d = context['d']
			if d > 0 and int(a) != 0:
				context['descr'] = 'Дискриминант: %d' %d
				context['x1'] = (-float(b) + float(d) ** (1/2.0)) / 2*float(a)
				context['x2'] = (-float(b) - float(d) ** (1/2.0)) / 2*float(a)
				print context['x2']
				print context['x1']
				context['result'] = "Квадратное уравнение имеет два действительных корня: x1 = %.1f, x2 = %.1f" % (context['x1'] + 0, context['x2'] + 0) 
			elif d < 0:
				context['descr'] = 'Дискриминант: %d' %d
				context['result'] = "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
			elif d == 0 and int(a) != 0:
				context['descr'] = 'Дискриминант: %d' %d
				context['x1'] = (-float(b) + float(d) ** (1/2.0)) / 2.0*float(a)
				context['result'] = "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %.1f" % (context['x1'] + 0)      
	else:
		form = QuadraticForm()

	context['form'] = form    
	return render(request, 'quadratic/results.html', context)