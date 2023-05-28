from django.urls import path
from .views import (my_profile_view,
                    invites_received_view,
                    profiles_list_view,
                    invite_profile_list_view,
                    ProfileListView,
                    send_invatation,
                    remove_from_friends,
                    accept_invatation,
                    reject_invatation,
                    ProfileDetailView,
                    reject_sent_invatation,
                    )

app_name = 'profiles'

urlpatterns = [
    path('my_profile/', my_profile_view, name='my_profile'),
    path('my_invites/', invites_received_view, name='my_invites'),
    path('', ProfileListView.as_view(), name='profile_list'),
    path('to_invite/', invite_profile_list_view, name='invite_profiles'),
    path('send_invite/', send_invatation, name='send_invite'),
    path('remove_friend/', remove_from_friends, name='remove_friend'),
    path('my_invites/accept/', accept_invatation, name='accept_invite'),
    path('my_invites/reject/', reject_invatation, name='reject_invite'),
    path('to_invite/reject/', reject_sent_invatation, name='reject_sent_invatations'),
    path('<slug>/', ProfileDetailView.as_view(), name='profile_detail_view'),
]