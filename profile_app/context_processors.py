from .models import Profile, Relationship

def profile_pic(request):
    if request.user.is_authenticated:
        profile_obj = Profile.objects.get(user=request.user)
        pic = profile_obj.avatar
        return {'picture': pic}
    return {}

def received_invites(request):
    if request.user.is_authenticated:
        profile_obj = Profile.objects.get(user=request.user)
        invites_num = Relationship.objects.invatations_recieved(receiver=profile_obj).count()
        return {'invites_num': invites_num}
    return {}