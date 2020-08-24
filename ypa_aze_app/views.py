from django.shortcuts import render
from .models import Meeting

def home(request):
    context = {
        'title': 'Əsas səhifə'
    }
    return render(request, 'home.html', context)

def about(request):
    context = {
        'title': 'Haqqında'
    }

    return render(request, 'about.html', context)

def schedule_of_teams(request):
    context = {
        'title':'Yarış cədvəli',
        'meetings':Meeting.objects.order_by('time')
    }   
    return render(request,'schedule_of_teams.html',context)

def contact(request):
    context = {
        'title': 'Əlaqə'
    }
    return render(request, 'contact.html', context)

def team(request):
    context = {
        'title': 'Komanda'
    }
    return render(request, 'team.html', context)