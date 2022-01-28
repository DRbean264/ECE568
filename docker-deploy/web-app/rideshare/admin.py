from django.contrib import admin
from .models import UserProfile, Vehicle, OwnerRide, SharerRide

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Vehicle)
admin.site.register(OwnerRide)
admin.site.register(SharerRide)
