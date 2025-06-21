from django.urls import path
from accounts import views

urlpatterns = [
    path('', views.IsoLoginView, name=''),
    path('IsoSignUpView', views.IsoSignUpView, name='IsoSignUpView'),
    path('IsoHome', views.IsoHome, name='IsoHome'),
    path('IsoLogoutView', views.IsoLogoutView, name='IsoLogoutView'),
]