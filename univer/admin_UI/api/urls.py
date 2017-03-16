from django.conf.urls import url, include
import views

urlpatterns = [
    url(r'^subject/(?P<pk>[0-9]+)', views.subjects_list),
    url(r'^shedul/', views.get_shedul),
    url(r'^grouop/(?P<pk>[0-9]+)', views.group_get),
    url(r'^currentweek/', views.get_cur_week),
]
