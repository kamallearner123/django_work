"""
URL configuration for blogs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import include

def home_view(request):
    return render(request, "home.html", {"message": "Welcome to the Home Page!"})
    #return HttpResponse("Welcome to the Home Page!")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", home_view, name="home"),
    path("ai/", include("ai.urls")), # routing the url resolution to ai.urls
    #path("blockchain/", include("blockchain.urls")), # routing the url resolution to blockchain.urls
]
