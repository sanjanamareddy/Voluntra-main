from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name = 'main'),
    path('login', views.login, name = 'login'),
    path('aboutUs', views.aboutUs, name = 'aboutUs'),
    path('myEvents', views.myEvents, name = 'myEvents'),
    path('eventDetails', views.eventDetails, name = 'eventDetails'),
    path('home', views.home, name = 'home'),
    path('login1', views.login1, name = 'login1'),
    path('signUp', views.signUp, name = 'signUp'),
    path('logout', views.logout, name = 'logout'),
    
    path('loginOrg', views.loginOrg, name = 'loginOrg'),
    path('loginVol', views.loginVol, name = 'loginVol'),



    path('joinEvent_1', views.joinEvent_1, name = 'joinEvent_1'),
    path('joinEvent_2', views.joinEvent_2, name = 'joinEvent_2'),
    path('joinEvent_3', views.joinEvent_3, name = 'joinEvent_3'),
    path('joinEvent_4', views.joinEvent_4, name = 'joinEvent_4'),

]