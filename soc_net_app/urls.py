from django.urls import path
from soc_net_app.views import MainPaige

urlpatterns = [
    path('home/', MainPaige.as_view(), name='home'),
]