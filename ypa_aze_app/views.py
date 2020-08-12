from django.shortcuts import render

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