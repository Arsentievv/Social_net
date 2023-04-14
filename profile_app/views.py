from django.shortcuts import render
from django.views import generic
from profile_app.models import Profile


# class MyProfileView(generic.DetailView):
#     model = Profile
#     context_object_name = 'profile'
#     template_name = 'profile_app/my_profile.html'

def my_profile_view(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'profile_app/my_profile.html', context={'profile': profile})


