from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='main/index.html')),
    path('about', TemplateView.as_view(template_name='main/about.html')),
    path('faq', TemplateView.as_view(template_name='main/faq.html')),
    path('price', TemplateView.as_view(template_name='main/price.html')),
    path('contact', TemplateView.as_view(template_name='main/contact.html')),
]