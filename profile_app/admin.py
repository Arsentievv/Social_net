from django.contrib import admin
from profile_app.models import Profile, Relationship


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
admin.site.register(Relationship)
