from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout



class Login(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
            
        return render(request, 'accounts/login.html')

    def post(self, request):
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        user = User.objects.filter(username=username).first()

        if not user:
            messages.error(request, 'User doesn\'t exist!')
            return redirect('login')

        if not user.check_password(password):
            messages.error(request, 'Password is wrong!')
            return redirect('login')

        login(request, user)
        return redirect('/')




class Logout(View):

    def get(self, request):
        logout(request)
        return redirect('/')