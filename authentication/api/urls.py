from django.conf.urls import url, include

from .views import (
	#Sighting_ListAPIView, 
	#Sighting_DetailAPIView,
	#Sighting_UpdateAPIView,
	#Sighting_DeleteAPIView,
	User_CreateAPIView,
	UserViewSet
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
#router.register(r'users', UserViewSet, base_name='user')
router.register(r'users', UserViewSet)

urlpatterns = [
    #url(r'^$', Sighting_ListAPIView.as_view(), name='list'),
    #url(r'^(?P<pk>\d+)/$', Sighting_DetailAPIView.as_view(), name='detail'),
    #url(r'^(?P<pk>\d+)/edit/$', Sighting_UpdateAPIView.as_view(), name='update'),
    #url(r'^(?P<pk>\d+)/delete/$', Sighting_DeleteAPIView.as_view(), name='remove'),
    url(r'^', include(router.urls)),
    url(r'^register/$', User_CreateAPIView.as_view(), name='register'),
]
