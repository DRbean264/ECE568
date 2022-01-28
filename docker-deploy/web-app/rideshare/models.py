from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


# validation functions here
def validate_positive(value):
    if value <= 0:
        raise ValidationError(
            gettext_lazy('The value should be positive')
        )


# Create your models here.
class UserProfile(models.Model):
    phoneNumber = PhoneNumberField('Phone Number', unique=True)
    birthday = models.DateField('Date of birth', blank=True, null=True)
    gender_choices = [(0, 'female'),
                      (1, 'male'),
                      (2, 'prefer not to tell')]
    gender = models.IntegerField('Gender', choices=gender_choices, blank=True, null=True)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    def __str__(self, *args, **kwargs):
        return str(self.user)

    def getFullName(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)

    def getGender(self):
        return self.gender_choices[self.gender][1]

class VehicleTypeInfo:
    max_capacity = [6, 2, 4, 6, 2, 7, 8, 4]
    type_choices = [(0, 'Sedan'),
                    (1, 'Coupe'),
                    (2, 'Sports Car'),
                    (3, 'Station Wagon'),
                    (4, 'Convertible'),
                    (5, 'Sport-Utility Vehicle'),
                    (6, 'Minivan'),
                    (7, 'Pickup Truck')]
    type_help_text = "-Sedan: traditional trunks with four doors<br/>\
    -Coupe: trunks with two doors<br/>\
    -Sports Car: the sportiest, hottest, coolest-looking coupes<br/>\
    -Station Wagon: similar to sedans but have an extended roofline and a hatch door at the rear instead of a trunk<br/>\
    -Convertible: the roof can be retracted into the body<br/>\
    -Sport-Utility Vehicle(SUV): taller and boxier than sedans, offer an elevated seating position<br/>\
    -Minivan: spacial cars which have adjustable seats in their second and third rows<br/>\
    -Pickup Truck: have passenger cabs and open cargo beds in the rear"


class Vehicle(models.Model):
    vtinfo = VehicleTypeInfo()
    vehicleType = models.IntegerField('Vehicle Type',
                                      choices=vtinfo.type_choices,
                                      help_text=vtinfo.type_help_text)
    plateNum = models.CharField('License Plate Number', max_length=20)
    specialInfo = models.CharField("Special info about your vehicle (optional)", max_length=200, blank=True)
    driver = models.OneToOneField(User,
                                  on_delete=models.CASCADE,
                                  default=None)

    def __str__(self, *args, **kwargs):
        return self.vtinfo.type_choices[self.vehicleType][1]

    def capacity(self):
        return self.vtinfo.max_capacity[self.vehicleType]

    def getVehicleType(self):
        return self.vtinfo.type_choices[self.vehicleType][1]


class OwnerRide(models.Model):
    destaddr = models.TextField('Destination Address', max_length=400)
    arrivalTime = models.DateTimeField('Desired Arrival Time')
    numPassengers = models.IntegerField('Number of Passengers',
                                        validators=[validate_positive])

    vtinfo = VehicleTypeInfo()
    vehicleType = models.IntegerField('Desired Vehicle Type',
                                      choices=vtinfo.type_choices,
                                      help_text=vtinfo.type_help_text)
    shareable = models.BooleanField("Do you want to share this ride with others?", default=False)
    specialRequest = models.CharField("Special requests about the vehicle you want (optional)", max_length=200, blank=True)
    confirmed = models.BooleanField("The is confirmed by a driver or not", default=False)
    completed = models.BooleanField("This ride is completed or not", default=False)

    user = models.ForeignKey(verbose_name='User who request the ride', to=User, on_delete=models.CASCADE, default=None)
    vehicle = models.ForeignKey(verbose_name='Vehicle & driver for this ride', to=Vehicle, on_delete=models.CASCADE, default=None, blank=True, null=True)

    def __str__(self):
        return self.user.userprofile.getFullName() + ' - ' + \
            self.destaddr

    def totalPassengerNum(self):
        num = self.numPassengers
        for ride in self.sharerride_set.all():
            num += ride.numPassengers
        return num

    def getVehicleType(self):
        return self.vtinfo.type_choices[self.vehicleType][1]

class SharerRide(models.Model):
    ownerride = models.ForeignKey(verbose_name="The ride chosen to join",
                                  to=OwnerRide, on_delete=models.CASCADE)
    user = models.ForeignKey(
        verbose_name='The user who requests the ride',
        to=User, on_delete=models.CASCADE
    )
    numPassengers = models.IntegerField('Number of Passengers',
                                        validators=[validate_positive])

    def __str__(self):
        return self.user.userprofile.getFullName()
