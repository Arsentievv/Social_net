from django.urls import path
from .views import MainPaige

urlpatterns = [
    path('home/', MainPaige.as_view(), name='home'),
]