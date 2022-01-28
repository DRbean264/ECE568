"""rideshAareservice UARL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from rideshare.views import home_view, driver_register_view,\
    display_profile_view, ride_request_view, open_ride_view,\
    confirmed_ride_view, completed_ride_view, edit_ride_view,\
    ride_detail_view, ride_join_view, join_confirm_view,\
    all_rides_view, make_a_drive_view, drive_confirm_view,\
    confirmed_ride_driver_view, completed_ride_driver_view,\
    quit_joined_view, mark_complete_view
from register.views import register_view, UserPasswordsChangeView


urlpatterns = [
    path('', home_view, name='home'),
    path('register/', register_view, name='register'),
    path('edit_profile/', display_profile_view, name='edit profile'),
    path('driver_register/', driver_register_view, name='driver register'),
    path('all_rides/', all_rides_view, name='all rides'),
    path('open_ride/', open_ride_view, name='open ride'),
    path('open_ride/<int:pk>/edit/', edit_ride_view.as_view(), name='edit open ride'),
    path('open_ride/<int:pk>/quit/', quit_joined_view, name='quit joined ride'),
    path('open_ride/<int:pk>/view/', ride_detail_view, name='view open ride'),
    path('confirmed_ride/', confirmed_ride_view, name='confirmed ride list'),
    path('confirmed_ride_driver/', confirmed_ride_driver_view, name='confirmed ride list'),
    path('confirmed_ride/<int:pk>/view/', ride_detail_view, name='view driver confirmed ride'),
    path('confirmed_ride_driver/<int:pk>/view/', ride_detail_view, name='view driver confirmed ride'),
    path('confirmed_ride_driver/<int:pk>/complete/', mark_complete_view, name='mark as completed'),
    path('completed_ride/', completed_ride_view, name='completed ride'),
    path('completed_ride_driver/', completed_ride_driver_view, name='driver completed ride'),
    path('completed_ride/<int:pk>/view/', ride_detail_view, name='view completed ride'),
    path('ride_request/', ride_request_view, name='ride request'),
    path('ride_join/', ride_join_view, name='ride join'),
    path('ride_join/<int:pk>/view/', ride_detail_view, name='view ride join'),
    path('ride_join/<int:pk>/join/', join_confirm_view, name='join ride'),
    path('make_a_drive/', make_a_drive_view, name="make a drive"),
    path('make_a_drive/<int:pk>/view', ride_detail_view, name="view make drive"),
    path('make_a_drive/<int:pk>/confirm', drive_confirm_view, name="confirm a drive"),
    path('password/', UserPasswordsChangeView.as_view()),
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
]
