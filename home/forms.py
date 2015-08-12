from django import forms

class ContactAgentForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    your_email = forms.EmailField(label='Your email', max_length=100)
    your_message = forms.CharField( widget=forms.Textarea )
