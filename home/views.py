from django.shortcuts import render

from .models import Listing
from .models import Agent
from .models import Gallery
from django.views.decorators.csrf import ensure_csrf_cookie


def index(request):
    featured = Listing.objects.filter(featured='yes');
    fourAgents = Agent.objects.order_by('order')[0:4]
    agents = Agent.objects.order_by('order')[:]
    gallery = Gallery.objects.order_by('title')[:];
    context = {'agents': agents, 'fourAgents':fourAgents, 'featured':featured, 'gallery':gallery}
    return render(request, 'home/index.html', context)

def listings(request):
    listings = Listing.objects.filter(published='yes').order_by('order')[:];
    gallery = Gallery.objects.order_by('title')[:];
    context = {'listings':listings, 'gallery':gallery}
    return render(request, 'home/listings.html', context)

def singleListing(request, listing_id = None, *args, **kwargs):
    listings = Listing.objects.filter(id=listing_id).order_by('order')[:]
    gallery = Gallery.objects.order_by('title')[:];
    context = {'listings': listings,'gallery':gallery}
    return render(request, 'home/single.html',context)

def singleAgent(request, agent_id = None, *args, **kwargs):
    agents = Agent.objects.filter(id=agent_id).order_by('order')[:]
    context = {'agents': agents}
    return render(request, 'home/profile.html',context)
