from django.shortcuts import render, redirect, get_object_or_404
#from django.http import HttpResponse
from django.http import Http404

from .forms import SightingForm
from .models import Sighting
from django.utils import timezone

# Create your views here.
def index(request):
    if request.method == "POST":
        form = SightingForm(request.POST)
        if form.is_valid():
        	sighting = form.save(commit=False)
        	sighting.datetime = timezone.now()
        	sighting.save()
        	return redirect('htwwg:detail', pk=sighting.pk)
        	#return render(request, 'htwwg/thank.html', {'title': 'Thank You'})
    else:
        form = SightingForm()

    return render(request, 'htwwg/index.html', {'form': form, 'title': 'Report a Possible sighting'})

def sighting_list(request):
	sightings = Sighting.objects.filter(datetime__lte=timezone.now()).order_by('datetime')
	return render(request, 'htwwg/sighting_list.html', {'sightings': sightings, 'title': 'Sighting Listing : '})

from django.http import Http404

def detail2(request, pk):
	sight = get_object_or_404(Sighting, pk=pk)
	return render(request, 'htwwg/thank.html', {})

def sighting_detail(request, pk):
	sight = get_object_or_404(Sighting, pk=pk)
	return render(request, 'htwwg/sighting_detail.html', {'sight': sight})
	#return render(request, 'htwwg/thank.html', {})
