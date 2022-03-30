from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('create', views.create, name='create'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('hsk1', views.hsk1, name='hsk1'),
    path('hsk2', views.hsk2, name='hsk2'),
    path('hsk3', views.hsk3, name='hsk3'),
    path('hsk4', views.hsk4, name='hsk4'),
    path('hsk5', views.hsk5, name='hsk5'),
    path('hsk6', views.hsk6, name='hsk6')

]
