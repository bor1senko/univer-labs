from django.conf.urls import url, include
import views

urlpatterns = [
    url(r'^subject/(?P<pk>[0-9]+)', views.subjects_list),
    url(r'^grouop/(?P<pk>[0-9]+)', views.group_get),
]
