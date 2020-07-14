from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('about/', include('about.urls', namespace='about')),
    path('team/', include('team.urls', namespace='team')),
    path('contact/', include('contact.urls', namespace='contact')),
]
