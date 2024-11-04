from django.views.generic import TemplateView
from django.shortcuts import render


# Create your views here.


class IndexView(TemplateView):
    template_name = 'service.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ServiceDetailView(TemplateView):
    template_name = 'service_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
