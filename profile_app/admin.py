from django.contrib import admin
from django.contrib import admin
from profile_app.models import Profile


# class ProfileAdmin(admin.ModelAdmin):
#     list_display = [
#         'first_name', 'last_name',
#         'bio', 'email', 'country',
#         'avatar', 'slug',
#         'updated', 'created'
#     ]
#
# admin.site.register(Profile, ProfileAdmin)
admin.site.register(Profile)