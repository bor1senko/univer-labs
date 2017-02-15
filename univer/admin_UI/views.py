    # -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from forms import SignUpForm
from django.contrib.auth import login, logout, authenticate



def index(request):
    return render(request, 'admin_UI/index.html')


def signup(request):
    if request.method == 'GET':
        form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'admin_UI/signup.html', {'form': form})


def signin(request):
    if request.user.is_authenticated():
        print request.user
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                print 1
                login(request, user)
                print 2
                return render(request, 'admin_UI/accaunt.html', {'user': user})
            else:
                return HttpResponse("этот аккаунт не активирован")
        else:
            return HttpResponseRedirect('/')
