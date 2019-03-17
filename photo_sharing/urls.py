from django.conf.urls import url
from django.contrib.auth.views import login, logout

from photo_sharing import views

urlpatterns = [
    url(r'^register/$', views.register_view, name='register'),
    url(r'^login/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'home.html',
                               'next_page': 'users:login'}, name='logout'),
    url(r'^(?P<username>[a-zA-Z0-9.+\-_@]+)/$', views.profile_view, name='profile'),
    # url(r'^search/$', views.search_user, name='search'),
    url(r'^(?P<username>[a-zA-Z0-9.+\-_@]+)/delete-photo/(?P<id>[0-9]+)/$',
        views.delete_photo, name='delete-photo'),
]
