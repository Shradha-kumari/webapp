from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
   path('',views.sign, name="sign"),
   path('postsign',views.postsign, name="postsign"),
   #path('adminshp',views.adminshp, name="adminshp")
]
