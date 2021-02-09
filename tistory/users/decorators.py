from django.shortcuts import redirect

def login_required(function):
    def wrap(request, *args, **kwargs):
        user = request.session.get('user')
        if user is None:
            return redirect('/user/login')
        return function(request, *args, **kwargs)
    return wrap