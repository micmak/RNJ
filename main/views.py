from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import View

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
            messages.error(request, 'User doesn\'t exist!')
            return redirect('upload_images')
        
        for img in request.FILES.getlist('images'):
            UserImage.objects.create(owner=client, image=img)

        messages.success(request, F'Images uploaded for user {client.username}')
        return redirect('upload_images')
