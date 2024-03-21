from django.contrib import admin
from .models import Destination,News, Subscription,Available_Trips,AllDestinations,UserFeedback
# Register your models here.

admin.site.register(Destination)
admin.site.register(News)
admin.site.register(Subscription)
admin.site.register(Available_Trips)
admin.site.register( AllDestinations)
admin.site.register(UserFeedback)