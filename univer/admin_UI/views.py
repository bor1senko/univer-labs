# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from forms import SignUpForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from models import Subject, GroupShedul, Teacher
import requests
import xmltodict



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

@login_required(login_url='/')
def accaunt(request):
    user = request.user
    if isinstance(user, Teacher):
        subjects = Subject.objects.filter(teacher=user)
        return render(request, 'admin_UI/account.html', {'user': user, 'subjects': subjects})
    else:
        return HttpResponseRedirect('/')

def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/account/')
            else:
                return render(request, 'admin_UI/not_active.html')
        else:
            return HttpResponseRedirect('/')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')
