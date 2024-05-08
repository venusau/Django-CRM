from django.contrib import admin
from django.urls import path, include #CHANGES: added the include  



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('website.urls')), #CHANGES: added the include  with the website.urls
]
