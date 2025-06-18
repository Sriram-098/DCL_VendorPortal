from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.startingpage,name="startingpage"),
    path("instruction/",views.instructionpage,name="instructionpage"),
    path("instructionregisteruser", views.instructionregisteruser, name="instructionregisteruser"),
    path("register",views.register,name="register")

]