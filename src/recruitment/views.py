from django.shortcuts import render
from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Recruitment App.'
        context['message'] = 'Greetings in our Lord and Savior!'
        return context
class ContactView(TemplateView):
    template_name = 'about.html'