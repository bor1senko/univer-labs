# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth import login, logout, authenticate
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from admin_UI.models import Faculty, Specialty, Group, Subject, Rating, Student, GroupShedul
from serializers import *
from datetime import datetime
import requests
import xmltodict

'''
class JsonRespons(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        #kwargs['content_type'] = 'aplication/json'
        super(JsonRespons, self).__init__(content, **kwargs)
'''
def get_cur_week(request):
    try:
        cur_week =  requests.get('https://www.bsuir.by/schedule/rest/currentWeek/date/{0}'.format(datetime.strftime(datetime.today(), "%d.%m.%Y"))).text
    except:
        cur_week = ""
    return JsonResponse({"curWeek": cur_week})

def get_shedul(request):
    if request.method == "GET":
        gname = request.GET['group_name']
        try:
            group = GroupShedul.objects.get(name=gname)
        except:
            group = None
        try:
            if group is not None:
                respons = requests.get('https://www.bsuir.by/schedule/rest/schedule/{0}'.format(group.idForShedul))
                respons = xmltodict.parse(respons.text)
            else:
                respons = False
        except:
            respons = False
        if group is not None:
            group = GroupShedulSerializer(group).data
        if respons != False:
            return JsonResponse({"group": group, "data": respons['scheduleXmlModels']['scheduleModel']})
        else:
            return JsonResponse({"group": group, "data": respons})

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
