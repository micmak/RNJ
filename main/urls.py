from django.urls import path
from django.views.generic import TemplateView

from .views import *


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
    path('parties-events', TemplateView.as_view(template_name='main/parties-events.html')),
    path('free', TemplateView.as_view(template_name='main/free.html')),
    path('black-white', TemplateView.as_view(template_name='main/black-white.html')),
    path('headshot', TemplateView.as_view(template_name='main/headshot.html')),
    path('gallery', TemplateView.as_view(template_name='main/gallery.html')),
    path('Patrick&Engy', TemplateView.as_view(template_name='main/Patrick&Engy.html')),
    path('LIAM&CAROLINE', TemplateView.as_view(template_name='main/LIAM&CAROLINE.html')),
    path('HANY&JACKLINE', TemplateView.as_view(template_name='main/HANY&JACKLINE.html')),
    path('EMIL&ANA', TemplateView.as_view(template_name='main/EMIL&ANA.html')),
    path('JOHN', TemplateView.as_view(template_name='main/JOHN.html')),
    path('ADRIAN&ALETA', TemplateView.as_view(template_name='main/ADRIAN&ALETA.html')),


  
    # path('add-image', TemplateView.as_view(template_name='main/add-image.html')),
    path('add-image', UploadImages.as_view(), name='upload_images'),
    path('sendmail', send_contact_email, name='sendmail')
]
