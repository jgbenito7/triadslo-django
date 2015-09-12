from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Listing
from .models import Agent
from .models import Gallery
from .models import Testimonial
from django.views.decorators.csrf import ensure_csrf_cookie
from .forms import ContactAgentForm
from django.core.mail import send_mail

def index(request):
    featured = Listing.objects.filter(featured='yes').order_by('order')[0:7];
    fourAgents = Agent.objects.order_by('order')[0:4]
    agents = Agent.objects.order_by('order')[:]
    gallery = Gallery.objects.order_by('title')[:]
    testimonials = Testimonial.objects.order_by('order')[:]
    context = {'agents': agents, 'fourAgents':fourAgents, 'featured':featured, 'gallery':gallery, 'testimonials':testimonials}
    return render(request, 'home/index.html', context)

def listings(request):
    listings = Listing.objects.filter(published='yes').order_by('order')[:];
    gallery = Gallery.objects.order_by('title')[:];
    context = {'listings':listings, 'gallery':gallery}
    return render(request, 'home/listings.html', context)

def comingSoon(request):
    listings = Listing.objects.filter(published='yes',status='coming_soon').order_by('order')[:];
    gallery = Gallery.objects.order_by('title')[:];
    context = {'listings':listings, 'gallery':gallery}
    return render(request, 'home/listings.html', context)

def agents(request):
    agents = Agent.objects.order_by('order')[:]
    context = {'agents':agents}
    return render(request, 'home/agents.html', context)

def singleListing(request, listing_id = None, *args, **kwargs):
    listings = Listing.objects.filter(id=listing_id).order_by('order')[:]
    allListings = Listing.objects.filter(published='yes').order_by('order')[:];
    gallery = Gallery.objects.order_by('title')[:];
    context = {'listings': listings,'gallery':gallery, 'allListings':allListings}
    return render(request, 'home/single.html',context)

def singleAgent(request, agent_id = None, *args, **kwargs):
    agents = Agent.objects.filter(id=agent_id).order_by('order')[:]
    allListings = Listing.objects.filter(published='yes').order_by('order')[:];
    gallery = Gallery.objects.order_by('title')[:];
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactAgentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['your_message']
            sender = form.cleaned_data['your_name']
            recipients = ['jgbenito7@gmail.com']
            send_mail(subject, message, sender, recipients)

            # redirect to a new URL:
            return HttpResponseRedirect('/listings/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactAgentForm()


    context = {'agents': agents, 'gallery':gallery, 'allListings':allListings, 'form':form}
    return render(request, 'home/profile.html', context)

def contactus(request):
    return render(request, 'home/contactus.html')
