# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from forms import SignUpForm
from django.contrib import messages

def index(request):
     return render(request, 'admin_UI/index.html')


def signup(request):
    if request.method == 'GET':
        form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'admin_UI/signup.html', {'form': form})
