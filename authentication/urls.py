from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),


    path('features', views.features, name='features'),
    path('ContactUs', views.ContactUs, name='ContactUs'),
    path('HealthAndSafety', views.HealthAndSafety, name='HealthAndSafety'),
    path('DiseasesRisks', views.DiseasesRisks, name='DiseasesRisks'),
    path('LegalAndPolicyServices', views.LegalAndPolicyServices, name='LegalAndPolicyServices'),
    
]
