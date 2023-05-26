from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import generic
from profile_app.models import Profile, Relationship
from .forms import ProfileModelForm
from django.db.models import Q



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


def invite_profile_list_view(request):
    user = request.user
    qs = Profile.objects.get_all_profiles_to_invite(sender=user)

    context = {
        'qs': qs,
    }

    return render(request, 'profile_app/invite_profiles.html', context=context)

def profiles_list_view(request):
    user = request.user
    qs = Profile.objects.get_all_profiles(me=user)

    context = {
        'qs': qs,
    }

    return render(request, 'profile_app/profiles_list.html', context=context)

class ProfileListView(generic.ListView):
    model = Profile
    template_name = 'profile_app/profiles_list.html'
    context_object_name = 'qs'

    def get_queryset(self):
        qs = Profile.objects.get_all_profiles(me=self.request.user)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = User.objects.get(username__iexact=self.request.user)
        profile = Profile.objects.get(user=user)
        rel_s = Relationship.objects.filter(receiver=profile)
        rel_r = Relationship.objects.filter(sender=profile)
        rel_receiver = []
        for item in rel_r:
            rel_receiver.append(item.receiver.user)
        rel_sender = []
        for item in rel_s:
            rel_sender.append(item.sender.user)
        context['rel_receiver'] = rel_receiver
        context['rel_sender'] = rel_sender
        context['is_empty'] = False
        if len(self.get_queryset()) == 0:
            context['is_empty'] = True
        return context

def send_invatation(request):
    if request.method == 'POST':
        pk = request.POST.get('profile_pk')
        user = request.user
        sender = Profile.objects.get(user=user)
        receiver = Profile.objects.get(pk=pk)
        rel = Relationship.objects.create(sender=sender, receiver=receiver, status='send')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('profiles:my_profile')

def remove_from_friends(request):
    if request.method == 'POST':
        pk = request.POST.get('profile_pk')
        user = request.user
        sender = Profile.objects.get(user=user)
        receiver = Profile.objects.get(pk=pk)

        rel = Relationship.objects.get(
            (Q(sender=sender) & Q(receiver=receiver) | (Q(sender=receiver) & Q(receiver=sender)))
        )
        rel.delete()
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('profiles:my_profile')


