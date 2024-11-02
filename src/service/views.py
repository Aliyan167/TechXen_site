from django.views.generic import TemplateView
from django.shortcuts import render


# Create your views here.


class IndexView(TemplateView):
    template_name = 'service.html'


class ServiceDetailView(TemplateView):
    template_name = 'service_detail.html'
