from django.shortcuts import render

from django.views.generic import TemplateView

from src.team.models import TeamMember


class IndexView(TemplateView):
    template_name = 'team.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

