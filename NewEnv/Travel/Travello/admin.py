from django.contrib import admin
from .models import Destination,bestTrips, Subscription,Available_Trips,AllDestinations
# Register your models here.

admin.site.register(Destination)
admin.site.register(bestTrips)
admin.site.register(Subscription)
admin.site.register(Available_Trips)
admin.site.register( AllDestinations)