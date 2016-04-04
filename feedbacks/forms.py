from django.db import models
from django import forms
from feedbacks.models import Feedback

class FeedbackForm(forms.ModelForm):
	class Meta:
		model = Feedback