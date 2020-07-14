from django.shortcuts import render

def team(request):
    context = {
        'title': 'Komanda ilə tanış'
    }
    return render(request, 'team/team.html', context)