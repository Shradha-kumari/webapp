
from ast import Global
from distutils.command.config import config
import email
import re
import string
from stringprep import in_table_c11
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate, login
from django.contrib.auth import authenticate, logout
from django.core.mail import send_mail
from django.contrib import messages
from virtualenv import session_via_cli
from LMS import settings
#import pyrebase5
from django.contrib import auth




def sign(request):
    return render(request, 'sign.html')

def postsign(request):


    email = request.POST.get('email')
    password = request.POST.get('password')




    if email == "shradha12karn@gmail.com":

        return render(request, 'managerhp.html')

    elif email == "shradha11karn@gmail.com":
        return render(request, 'adminshp.html')

    else:
        return render(request, 'userhp.html')


#code change from gui
