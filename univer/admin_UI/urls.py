from django.conf.urls import url, include
import views
import api

urlpatterns = [
    url(r'^$', views.index),
    url(r'^signup/', views.signup),
    url(r'^signin/', views.signin),
    url(r'^logout/', views.logout_user),
    url(r'^account/', views.accaunt),
    url(r'^api/', include('admin_UI.api.urls')),
]
