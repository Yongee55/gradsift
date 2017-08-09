# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone


# Create your views here.


class IndexView(generic.ListView):
    template_name = 'applicant/create_profile.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        return 0