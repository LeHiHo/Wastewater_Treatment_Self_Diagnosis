from django.contrib import admin
from django.urls import path, include

import firstapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', firstapp.views.index, name='index')
    path('', include('firstapp.urls')),
   
]
