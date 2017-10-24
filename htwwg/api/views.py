from django.conf.urls import url
from rest_framework.generics import (
	ListAPIView, 
	UpdateAPIView, 
	DestroyAPIView, 	
	RetrieveAPIView,
	RetrieveUpdateAPIView,
	CreateAPIView
) 

from rest_framework.permissions import (
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly
	)

from .serializers import SightingSerializer, SightingListSerializer

from htwwg.models import Sighting

class Sighting_ListAPIView(ListAPIView):
    """
    View to list all sightings in the system.

    """
    #authentication_classes = (authentication.TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)
    #permission_classes = (permissions.IsAdminUser,)
    #permission_classes = (AllowAny,)
    queryset = Sighting.objects.all()
    serializer_class = SightingListSerializer
    permission_classes = (AllowAny,)

class Sighting_CreateAPIView(CreateAPIView):
    queryset = Sighting.objects.all()
    serializer_class = SightingSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
    	serializer.save(name=self.request.name)

class Sighting_DeleteAPIView(DestroyAPIView):
    queryset = Sighting.objects.all()
    serializer_class = SightingSerializer
    permission_classes = (IsAuthenticated, IsAdminUser,)

class Sighting_DetailAPIView(RetrieveAPIView):
    queryset = Sighting.objects.all()
    serializer_class = SightingSerializer
    permission_classes = (AllowAny,)

class Sighting_UpdateAPIView(RetrieveUpdateAPIView):
    queryset = Sighting.objects.all()
    serializer_class = SightingSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
