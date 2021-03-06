"""assignment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import include

from photo_sharing import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home_view, name='home'),
    url(r'^users/', include(('photo_sharing.urls', 'photo_sharing'), namespace='users')),
    url(r'^upload-photo/$', views.upload_photo, name='upload-photo'),
    url(r'^search/$', views.search_user, name='search'),
]
