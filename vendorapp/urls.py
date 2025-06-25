from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.startingpage,name="startingpage"),
    path("instruction/",views.instructionpage,name="instructionpage"),
    path("instructionregisteruser", views.instructionregisteruser, name="instructionregisteruser"),
    path("register",views.register,name="register"),
    path('admin-dashboard/', views.admin_dashboard, name='admin-dashboard'),
    path('update-status/<int:vendor_id>/<str:new_status>/', views.update_status, name='update_status'),
    path('not-authorized/', views.not_authorized, name='not_authorized'),
    path("home/",views.home,name="home")


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)