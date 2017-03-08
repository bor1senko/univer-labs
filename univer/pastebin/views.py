from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from models import PostBin
from serialalezer import PostBinSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

'''
class JsonRespons(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        #kwargs['content_type'] = 'aplication/json'
        super(JsonRespons, self).__init__(content, **kwargs)
'''

def index(request):
    return render(request, 'pastebin/index.html')



def posts_list(request):
    print request.user
    if request.method == 'GET':
        posts = PostBin.objects.all()
        posts = PostBinSerializer(posts, many=True)
        return JsonResponse({"ans" :posts.data})
