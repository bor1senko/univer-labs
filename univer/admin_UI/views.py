    # -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from forms import SignUpForm
from django.contrib.auth import login, logout, authenticate



def index(request):
    if request.user.is_authenticated():
        user = request.user
    else:
        user = False
    return render(request, 'admin_UI/index.html', {'user': user})


def signup(request):
    if request.method == 'GET':
        form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'admin_UI/signup.html', {'form': form})


def accaunt(request):
    user =request.user
    return render(request, 'admin_UI/accaunt.html', {'user': user})


def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/accaunt/')
            else:
                return render(request, 'admin_UI/not_active.html')
        else:
            return HttpResponseRedirect('/')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')

            
