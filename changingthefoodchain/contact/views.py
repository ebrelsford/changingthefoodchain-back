from django.core.mail import mail_managers
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.generic import FormView

from .forms import ContactForm


class ContactView(FormView):
    form_class = ContactForm

    def form_invalid(self, form):
        return HttpResponseBadRequest('NOT OK')

    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        mail_managers('Someone just got in contact!', """
From: %s
Subject: %s

%s""" % (cleaned_data['email'], cleaned_data['subject'], cleaned_data['text']))
        return HttpResponse('OK')
