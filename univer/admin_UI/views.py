# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse

def index(request):
     return render(request, 'admin_UI/index.html')
