from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from django.core.mail import send_mail
from .models import UserImage


class UploadImages(View):
    def get(self, request):
        context = {
            'users': User.objects.all()
        }
        return render(request, 'main/add-image.html', context)


    def post(self, request):
        client = User.objects.filter(username=request.POST.get('client', None)).first()

        if not client:
            return JsonResponse({'msg': 'Please select a client'}, status=400)
        
        for img in request.FILES.getlist('images'):
            UserImage.objects.create(owner=client, image=img)
        
        return JsonResponse({'msg': 'Uploaded successfuly'})


from django.urls import resolve

def send_contact_email(request):
    email = request.POST.get('email', None)
    name = request.POST.get('name', None)
    subject = request.POST.get('subject', None)
    message = request.POST.get('message', None)
    origin = request.POST.get('origin', None)

    msg = F'You have new contact request\n\nUser : {name}\nSubject: {subject}\nMessage :{message}'
    send_mail('New contact request', msg, 'info@rnjphotography.co.uk', ['info@rnjphotography.co.uk'])
    return redirect(origin)