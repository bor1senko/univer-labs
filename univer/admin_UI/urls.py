from django.conf.urls import url, include
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^signup/', views.signup),
]
