from django.shortcuts import render, redirect
from django.contrib.auth.views import PasswordChangeView, PasswordChangeForm
from django.urls import reverse_lazy
from .forms import RegisterForm
from rideshare.forms import UserProfileForm


# Create your views here.
class UserPasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = '/edit_profile'
    template_name = 'registration/change-password.html'


def register_view(request, *args, **kwargs):
    register_message = "Ride Sharing Service Account Registration"

    if request.method == "POST":
        form = RegisterForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect("/login")
    else:
        form = RegisterForm()
        profile_form = UserProfileForm()

    context = {
        'register_message': register_message,
        'form': form,
        'profile_form': profile_form,
    }
    return render(request, 'register/register.html', context=context)
