from django.conf.urls import url

from .views import (
	Sighting_ListAPIView, 
	Sighting_DetailAPIView,
	Sighting_UpdateAPIView,
	Sighting_DeleteAPIView,
	Sighting_CreateAPIView
)
#app_name = 'htwwg'
urlpatterns = [
    url(r'^$', Sighting_ListAPIView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', Sighting_DetailAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/edit/$', Sighting_UpdateAPIView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', Sighting_DeleteAPIView.as_view(), name='remove'),
    url(r'^create/$', Sighting_CreateAPIView.as_view(), name='add'),
]