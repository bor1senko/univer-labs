from django.conf.urls import url, include
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^signup/', views.signup),
    url(r'^signin/', views.signin),
    url(r'^logout/', views.logout_user),
    url(r'^accaunt/', views.accaunt),
]
