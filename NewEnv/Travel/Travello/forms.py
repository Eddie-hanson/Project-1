from django import forms
from django.forms import ModelForm
from .models import Subscription, UserFeedback

class SubscriptionForm(ModelForm):
    class Meta:
        model=Subscription
        fields='__all__'
        widgets={'Name':forms.TextInput(attrs={'class':'newsletter_input newsletter_input_name', 'id':'newsletter_input_name','placeholder':'Name' , 'required':'required'}),
                 'Email':forms.TextInput(attrs={'class':'newsletter_input newsletter_input_email', 'id':'newsletter_input_email', 'placeholder':'Your e-mail' ,'required':"required"})
                 }
        
class UserFeedbackForm(forms.ModelForm):
    class Meta:
        model=UserFeedback
        fields='__all__'
        widgets={'Name': forms.TextInput(attrs={'class':'contact_input contact_input_name inpt'}),
                 'Email': forms.TextInput(attrs={'class':'contact_input contact_input_email inpt', 'placeholder':'Your e-mail' ,'required':"required"}),
                 'Subject': forms.TextInput(attrs={'class':'contact_input contact_input_subject inpt'}),
                 'Message': forms.Textarea(attrs={'class':'contact_textarea contact_input inpt'})
                 }
       