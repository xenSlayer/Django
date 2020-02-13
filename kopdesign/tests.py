def get_user(request):
    username = str(request.user)
    return username
get_user(request=get_user())