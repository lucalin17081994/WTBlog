def profile_picture(request):
    if request.user.is_authenticated:
        profile = request.user.profile
        return {'profile': profile}
    return {}
