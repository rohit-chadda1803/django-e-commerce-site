# NOTE: WE HAVE TO CREATE THIS FILE OURSELF. 
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name = "bloghome"),
    path('blogpost/<int:myid>',views.blogpost,name = "blogpost"),

]