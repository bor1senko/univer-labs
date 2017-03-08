# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth import login, logout, authenticate
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from admin_UI.models import Faculty, Specialty, Group, Subject, Rating, Student
from serializers import SubjectInfoSerializer, SubjectSerializer

'''
class JsonRespons(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        #kwargs['content_type'] = 'aplication/json'
        super(JsonRespons, self).__init__(content, **kwargs)
'''

def subject_detail(request, pk):
    user = request.user
    if request.method == 'GET':
        subject = SubjectSerializer(Subject.objects.get(pk=pk))
        return JsonResponse({'data': subject.data})
    if request.method == 'DELETE':
        pass

def subjects_list(request, pk=0):
    if request.method == 'GET':
        if request.user.is_authenticated():
            user = request.user
        subjects = SubjectInfoSerializer(Subject.objects.get(pk=pk))
        return JsonResponse({'data': subjects.data})

    if request.method == 'POST':
        pass


def group_get(request, pk):
    if request.method == 'GET':
        pass
