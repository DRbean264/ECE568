from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User


# Create your models here.
# class RideShareServiceUser(models.Model):
#     firstName = models.CharField('First Name', max_length=100)
#     middleName = models.CharField('Middle Name',
#                                   max_length=100, blank=True)
#     lastName = models.CharField('Last Name', max_length=100)
#     phoneNumber = PhoneNumberField('Phone Number', unique=True)
#     email = models.EmailField('Email', unique=True)
#     birthday = models.DateField('Date of birth')

#     gender_choices = [(0, 'female'),
#                       (1, 'male'),
#                       (2, 'prefer not to tell')]
#     gender = models.IntegerField('Gender', choices=gender_choices)
