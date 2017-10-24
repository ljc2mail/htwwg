from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^add/$', views.index, name='index'),
 	url(r'^$', views.sighting_list, name='sighting_list'), 
 	#url(r'^(?P<pk>\d+)/$', views.sighting_detail2, name='detail'),
 	url(r'^(?P<pk>\d+)/$', views.sighting_detail, name='detail'),
]