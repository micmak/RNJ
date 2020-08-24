from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='main/index.html')),
    path('about', TemplateView.as_view(template_name='main/about.html')),
    path('faq', TemplateView.as_view(template_name='main/faq.html')),
    path('wedding', TemplateView.as_view(template_name='main/wedding.html')),
    path('contact', TemplateView.as_view(template_name='main/contact.html')),
    path('maternity', TemplateView.as_view(template_name='main/maternity.html')),
    path('newborn', TemplateView.as_view(template_name='main/newborn.html')),
    path('children-family', TemplateView.as_view(template_name='main/children-family.html')),
    path('cake-smash', TemplateView.as_view(template_name='main/cake-smash.html')),
    path('free', TemplateView.as_view(template_name='main/free.html')),
    path('black-white', TemplateView.as_view(template_name='main/black-white.html')),
    path('headshot', TemplateView.as_view(template_name='main/headshot.html')),
    path('outdoor', TemplateView.as_view(template_name='main/outdoor.html')),
    path('gallery', TemplateView.as_view(template_name='main/gallery.html')),

]