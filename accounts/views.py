from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.
import base64
import hashlib
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from django.urls import reverse
from django.contrib import messages 
from accounts.decorators import custom_authenticate
from accounts.models import Users


def IsoHashPassword(username: str, password: str, salt: bytes = b'authsalt'):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt + username.encode(),
        iterations=100000,
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode())).decode()

def IsoLoginView(request):
    try:
        if request.method == 'POST':
            isoUsername = request.POST.get('username')
            isoPassword = request.POST.get('password')
            isoUserDetails = Users.objects.filter(username = isoUsername).first()
            if isoUserDetails:
                if isoUserDetails.password ==  IsoHashPassword(isoUsername,isoPassword):
                    request.session['is_loggedin'] = True
                    request.session['username'] = isoUserDetails.username
                    return redirect(reverse('IsoHome'))
            messages.error(request,'Invalid Username\Password')
            return redirect(reverse(''))
        else:
            return render(request,'IsoLogin.html')
    except Exception as isoex:
        messages.error(request,'Invalid Username\Password')
        return render(request,'IsoLogin.html')

def IsoSignUpView(request):
    try:
        if request.method == "POST":
            isoUsername = request.POST.get('username')
            isoPassword = request.POST.get('password')
            Users.objects.create(username = isoUsername, password = IsoHashPassword(isoUsername, isoPassword))
            return redirect(reverse(''))
        else:
            return render(request,'IsoSignUp.html')
    except Exception as isoex:
        messages.error(request,'Username Already Exists')
        return render(request,'IsoSignUp.html')

@custom_authenticate
def IsoHome(request):
    try:
        return render(request,'IsoHome.html',{'isoBrUsername':request.session.get('username')})
    except:
        messages.error(request,'Something Went Wrong')
        return render(request,'IsoHome.html',{'isoBrUsername':request.session.get('username')})

def IsoLogoutView(request):
    try:
        request.session.flush()
    except:
        return redirect(reverse(''))
    finally:
        return redirect(reverse(''))