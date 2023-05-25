from django.urls import path
from .views import (my_profile_view,
                    invites_received_view,
                    profiles_list_view,
                    invite_profile_list_view,
                    ProfileListView)

app_name = 'profiles'

urlpatterns = [
    path('my_profile/', my_profile_view, name='my_profile'),
    path('my_invites/', invites_received_view, name='my_invites'),
    path('profiles_list/', ProfileListView.as_view(), name='profile_list'),
    path('invite_profiles/', invite_profile_list_view, name='invite_profiles'),
]