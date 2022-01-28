from django import forms
from .models import UserProfile, Vehicle, OwnerRide
from django.contrib.auth.forms import UserChangeForm
from django.contrib.admin.widgets import AdminSplitDateTime, AdminDateWidget
from datetime import datetime
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .mywidgets import DateSelectorWidget


# validation functions
def validate_positive(value):
    if (value <= 0):
        raise ValidationError("Should be postive!")


# extended user model
class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['phoneNumber', 'birthday', 'gender']


# built in user model
class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password']


# vehicle register form
class DriverProfileForm(forms.ModelForm):

    class Meta:
        model = Vehicle
        fields = ['vehicleType', 'plateNum', 'specialInfo']


class RideRequestForm(forms.ModelForm):
    destaddr = forms.CharField(
        label="Destination Address",
        widget=forms.Textarea(
            attrs={'cols': '10', 'rows': '5',
                   'placeholder': 'Enter your address here.'}),
        min_length=0,
        max_length=400
    )
    arrivalTime = forms.DateTimeField(
        label="Desired Arrival Time (mm/dd/yyyy hh:mm:ss)",
        widget=DateSelectorWidget(),
    )

    class Meta:
        model = OwnerRide
        fields = ['destaddr', 'arrivalTime', 'numPassengers',
                  'vehicleType', 'shareable', 'specialRequest']
