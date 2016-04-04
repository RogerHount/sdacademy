from django.shortcuts import render
from django.views.generic.edit import CreateView
from feedbacks.models import Feedback
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


class FeedbackView(CreateView):
	model = Feedback
	template_name = "feedback.html"

	def get_context_data(self, **kwargs):
		context = super(FeedbackView, self).get_context_data(**kwargs)
		context['title'] = "Feedback"
		context['buttonname'] = "Leave feedback"
		return context

	def form_valid(self, form):
		feedback = form.save()
		messages.success(self.request, "Thank you for your feedback! We will keep in touch with you very soon!")
		send_mail(feedback.subject, feedback.message, settings.DEFAULT_FROM_EMAIL, [x[1] for x in settings.ADMINS], fail_silently=False)
		return super(FeedbackView, self).form_valid(form)

	def get_success_url(self):
		return reverse_lazy('feedback')