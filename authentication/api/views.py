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

from .serializers import UserCreateSerializer


from django.contrib.auth import get_user_model

User = get_user_model()

class User_CreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    #permission_classes = (IsAuthenticatedOrReadOnly,)

    #def perform_create(self, serializer):
    #	serializer.save(name=self.request.name)