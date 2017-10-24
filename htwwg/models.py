from django.db import models
from django.utils import timezone
# Create your models here.
class Sighting(models.Model):

	_FINS = (
		('Falcate','falcate'),
		('Traiangular', 'triangular'),
		('Rounded', 'rounded')
	)

	_WHALES = (
		('Humpback', 'humpback'),
		('Orca', 'orca')
	)

	_BLOWS = (
		('Tall', 'tall'),
		('Bushy', 'bushy'),
		('Dense', 'dense')
	)

	_WAVES = (
		('Flat', 'flat'),
		('Small', 'small'),
		('High', 'high')
	)

	name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	datetime =  models.DateTimeField(default=timezone.now)
	location = models.TextField()
	fin_type = models.CharField(max_length=30, choices=_FINS)
	whale_type = models.CharField(max_length=30, choices=_WHALES)
	blow_type = models.CharField(max_length=30, choices=_BLOWS)
	wave_type =  models.CharField(max_length=30, choices=_WAVES)
