from django.shortcuts import render
from functools import wraps

def custom_authenticate(isoViewFunction):
    @wraps(isoViewFunction)
    def IsoWrappedView(request, *args, **kwargs):
        if request.session.get('is_loggedin'):
            return isoViewFunction(request, *args, **kwargs)
        return render(request, '404.html', status=404)
    return IsoWrappedView