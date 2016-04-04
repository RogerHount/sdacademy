from django.shortcuts import render
from django.views.generic.edit import CreateView
from feedbacks.models import Course

# Create your views here.

class FeedbackView(CreateViewl):
	model = Feedback