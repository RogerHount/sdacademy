from django import forms
# -*- coding: utf-8 -*-

class QuadraticForm(forms.Form):
	a = forms.IntegerField(label='коэффициент a')
	b = forms.IntegerField(label='коэффициент b')
	c = forms.IntegerField(label='коэффициент c')


	def clean_a(self):
		if self.cleaned_data['a'] ==0:
			raise forms.ValidationError('коэффициент при первом слагаемом уравнения не может быть равным нулю')
		return self.cleaned_data


