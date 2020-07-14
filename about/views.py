from django.shortcuts import render

def about(request):
    context = {
        'title': 'Haqqında'
    }

    return render(request, 'about/about.html', context)