from django.forms import ModelForm
from .models import Subscription, UserFeedback

class SubscriptionForm(ModelForm):
    class Meta:
        model=Subscription
        fields='__all__'
        
class UserFeedbackForm(ModelForm):
    class Meta:
        model=UserFeedback
        fields='__all__'
       