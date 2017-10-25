from django import forms

from .models import Sighting

class SightingForm(forms.ModelForm):
    class Meta:
        model = Sighting
        fields = ('name', 'location', 'fin_type', 'whale_type', 'blow_type', 'wave_type',)