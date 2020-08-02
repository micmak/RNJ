from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='main/index.html')),
    path('about', TemplateView.as_view(template_name='main/about.html')),
    path('faq', TemplateView.as_view(template_name='main/faq.html')),
    path('wedding', TemplateView.as_view(template_name='main/wedding.html')),
    path('contact', TemplateView.as_view(template_name='main/contact.html')),
    path('pregnant', TemplateView.as_view(template_name='main/pregnant.html')),
    path('login', TemplateView.as_view(template_name='main/login.html')),
    path('regestration', TemplateView.as_view(template_name='main/regestration.html')),


]