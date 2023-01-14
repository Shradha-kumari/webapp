
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
import pyrebase
from django.contrib import auth

config = {
    """
  "apiKey": "AIzaSyBh54bhUiOduOlyq6k6DTTeXL_lAg0L94w",
  "authDomain": "cpanel-10ae6.firebaseapp.com",
  "databaseURL":"https://cpanel-10ae6-default-rtdb.firebaseio.com",
  "projectId": "cpanel-10ae6",
  "storageBucket": "cpanel-10ae6.appspot.com",
  "messagingSenderId": "206710126999",
  "appId": "1:206710126999:web:ee4da3d9d3f7de6bd4ecd2"
  """

  "apiKey": "AIzaSyBhZVv55hWtbdKavDvs-F4Vzmbbm60cEAE",
  "authDomain": "ecap-80609.firebaseapp.com",
  "databaseURL": "https://ecap-80609-default-rtdb.firebaseio.com",
  "projectId": "ecap-80609",
  "storageBucket": "ecap-80609.appspot.com",
  "messagingSenderId": "115895690408",
  "appId": "1:115895690408:web:16fb66783ae4ed5d8e0e9d",
  "measurementId": "G-N3PB3RFQX0"
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()







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


#code change from nand  demo