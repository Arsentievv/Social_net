from django.shortcuts import render
from django.views import generic
from profile_app.models import Profile, Relationship
from .forms import ProfileModelForm


# class MyProfileView(generic.DetailView):
#     model = Profile
#     context_object_name = 'profile'
#     template_name = 'profile_app/my_profile.html'

def my_profile_view(request):
    profile = Profile.objects.get(user=request.user)
    form = ProfileModelForm(request.POST or None, request.FILES or None, instance=profile)
    confirm = False
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            confirm = True

    context = {
        'profile': profile,
        'form': form,
        'confirm': confirm,
    }

    return render(request, 'profile_app/my_profile.html', context=context)


def invites_received_view(request):
    profile = Profile.objects.get(user=request.user)
    qs = Relationship.objects.invatations_recieved(receiver=profile)

    context = {
        'qs': qs,
    }

    return render(request, 'profile_app/my_invites.html', context=context)


def profiles_list_view(request):
    user = request.user
    qs = Profile.objects.get_all_profiles(me=user)

    context = {
        'qs': qs,
    }

    return render(request, 'profile_app/profiles_list.html', context=context)


def invite_profile_list_view(request):
    user = request.user
    qs = Profile.objects.get_all_profiles_to_invite(sender=user)

    context = {
        'qs': qs,
    }

    return render(request, 'profile_app/invite_profiles.html', context=context)