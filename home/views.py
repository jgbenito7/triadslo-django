from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Listing
from .models import Agent
from .models import Gallery
from .models import Testimonial
from .models import BestOfSlo
from django.views.decorators.csrf import ensure_csrf_cookie
from .forms import ContactAgentForm
from .forms import RequestShowingForm
from .forms import ContactUsForm
from django.core.mail import send_mail
from TwitterAPI import TwitterAPI

def index(request):
    featured = Listing.objects.filter(featured='yes').order_by('order')[0:7];
    fourAgents = Agent.objects.order_by('order')[0:4]
    agents = Agent.objects.order_by('order')[:]
    gallery = Gallery.objects.order_by('title')[:]
    testimonials = Testimonial.objects.order_by('order')[:]
    api = TwitterAPI("Z6F4io8VZiTx60XdtMU4EM0kf", "93QSIFfLsj3kewcEW6SjO0Jk1sqyphfGZxFIlmb9ktePXylIW5", "2463659724-xHhmNvIwBfjLA8SRdePR07vzWKUCTVCLmG6ErEK", "ZRR1GssUBUiPtQNsJMHhdHT5OzMEBxwaxkF4Vh4G50LW8")
    r = api.request('statuses/user_timeline',{'count':1})
    twitterText = ""
    for item in r.get_iterator():
        if 'text' in item:
            twitterText =  item['text']
    context = {'agents': agents, 'fourAgents':fourAgents, 'featured':featured, 'gallery':gallery, 'testimonials':testimonials, 'twitterText':twitterText}
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
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RequestShowingForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            subject = "Request For Showing: " + form.cleaned_data['listing_name']
            message = 'From: ' + form.cleaned_data['your_name'] + '\n' + '\n' + 'Email: ' + form.cleaned_data['your_email'] + '\n' + '\n' + 'Phone Number: ' + form.cleaned_data['your_phone'] + '\n' + '\n' + 'Message: ' + '\n' + '\n' + form.cleaned_data['your_message']
            sender = form.cleaned_data['your_name']
            recipients = ["info@triadslo.com"]
            send_mail(subject, message, sender, recipients)

            # redirect to a new URL:
            return HttpResponseRedirect('/listings/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = RequestShowingForm()

    context = {'listings': listings,'gallery':gallery, 'allListings':allListings, 'form':form}
    return render(request, 'home/single.html',context)

def singleAgent(request, agent_id = None, *args, **kwargs):
    agents = Agent.objects.filter(id=agent_id).order_by('order')[:]
    allListings = Listing.objects.filter(published='yes').order_by('order')[:];
    gallery = Gallery.objects.order_by('title')[:];
    testimonials = Testimonial.objects.filter(agent__id = agent_id)[:]
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactAgentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = 'From: ' + form.cleaned_data['your_name'] + '\n' + '\n' + 'Email: ' + form.cleaned_data['your_email'] + '\n' + '\n' + 'Phone Number: ' + form.cleaned_data['your_phone'] + '\n' + '\n' + 'Message: ' + '\n' + '\n' + form.cleaned_data['your_message']
            sender = form.cleaned_data['your_name']
            recipients = [form.cleaned_data['agent_email']]
            send_mail(subject, message, sender, recipients)

            # redirect to a new URL:
            return HttpResponseRedirect('/agents/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactAgentForm()


    context = {'agents': agents, 'gallery':gallery, 'allListings':allListings, 'form':form, 'testimonials':testimonials}
    return render(request, 'home/profile.html', context)

def contactus(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactUsForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            subject = "Message From www.triadslo.com"
            message = 'From: ' + form.cleaned_data['your_first_name'] + " " + form.cleaned_data['your_last_name'] + '\n' + '\n' + 'Email: ' + form.cleaned_data['your_email'] + '\n' + '\n' + 'Subject: ' + form.cleaned_data['subject']+ '\n' + '\n' + 'Phone Number: ' + form.cleaned_data['your_phone'] + '\n' + '\n' + 'Message: ' + '\n' + '\n' + form.cleaned_data['your_message']
            sender = form.cleaned_data['your_first_name'] + " " + form.cleaned_data['your_last_name']
            recipients = ["info@triadslo.com"]
            send_mail(subject, message, sender, recipients)
            # redirect to a new URL:
            return HttpResponseRedirect('/contactus/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactUsForm()


    context = {'form':form}
    return render(request, 'home/contactus.html',context)

def searchListings(request):
    return render(request, 'home/searchlistings.html')

def searchForclosures(request):
    return render(request, 'home/searchforclosures.html')

def bestOf(request, agent_id = None, *args, **kwargs):
    things = BestOfSlo.objects.filter(category='Things To Do')[:];
    places = BestOfSlo.objects.filter(category='Places To See')[:];
    dine = BestOfSlo.objects.filter(category='Wine and Dine')[:];
    allBestOf = BestOfSlo.objects.order_by('order')[:];
    context = {'things':things, 'places':places, 'dine':dine, 'allBestOf':allBestOf}
    return render(request, 'home/bestofslo.html', context)
