from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('team/',views.team,name='team'),
    path('contact/',views.contact,name='contact'),
    path('schedule_of_teams/',views.schedule_of_teams,name='schedule_of_teams')
]
