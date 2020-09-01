from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
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
            return JsonResponse({'msg': 'Please select a client'}, status=400)
        
        for img in request.FILES.getlist('images'):
            UserImage.objects.create(owner=client, image=img)
        
        return JsonResponse({'msg': 'Uploaded successfuly'})