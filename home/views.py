from django.shortcuts import render

def home(request):
    context = {
        'title': 'Əsas səhifə'
    }
    return render(request, 'home/home.html', context)