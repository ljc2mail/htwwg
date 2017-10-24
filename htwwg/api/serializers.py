from rest_framework.serializers import (
	ModelSerializer, 
	HyperlinkedIdentityField,
	SerializerMethodField
	)

#from profiles.serializers import ProfileSerializer

from htwwg.models import Sighting

class SightingListSerializer(ModelSerializer):
	url = HyperlinkedIdentityField(
		view_name='api-sighting:detail', 
		lookup_field='pk')

	class Meta:
		model=Sighting
		fields = ('url', 'name', 'datetime')
		#fields = ('name',  'url')

class SightingSerializer(ModelSerializer):

	class Meta:
		model=Sighting
		fields = '__all__'


class SightingCreateSerializer(ModelSerializer):

	class Meta:
		model=Sighting
		#fields = ('name', 'email', 'datetime', 'whale_type', 'blow_type', 'wave_type')
		fields = '__all__'
