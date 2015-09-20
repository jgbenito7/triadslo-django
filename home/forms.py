from django import forms

class ContactAgentForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    your_email = forms.EmailField(label='Your email', max_length=100)
    your_phone = forms.CharField(label='Your phone number', max_length=20)
    subject = forms.CharField(label='Subject', max_length=100)
    your_message = forms.CharField( widget=forms.Textarea )
    agent_email = forms.EmailField(label='Your email', max_length=100)

class RequestShowingForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    your_email = forms.EmailField(label='Your email', max_length=100)
    your_phone = forms.CharField(label='Your phone number', max_length=20)
    subject = forms.CharField(label='Subject', max_length=100)
    your_message = forms.CharField( widget=forms.Textarea )
    listing_name = forms.CharField(label='Listing Name', max_length=100)

class ContactUsForm(forms.Form):
    your_first_name = forms.CharField(label='Your First name', max_length=100)
    your_last_name = forms.CharField(label='Your Last name', max_length=100)
    your_email = forms.EmailField(label='Your email', max_length=100)
    your_phone = forms.CharField(label='Your phone number', max_length=20)
    subject = forms.CharField(label='Subject', max_length=100)
    your_message = forms.CharField( widget=forms.Textarea )
