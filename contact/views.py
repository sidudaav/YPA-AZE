from django.shortcuts import render

def contact(request):
    context = {
        'title': 'Əlaqə'
    }
    return render(request, 'contact/contact.html', context)