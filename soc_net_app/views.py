from django.shortcuts import render
from django.views import generic


class MainPaige(generic.TemplateView):
    template_name = 'soc_net_app/home.html'

