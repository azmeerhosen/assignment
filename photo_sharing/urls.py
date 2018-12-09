from django.urls import path
from photo_sharing import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    path(r'^<username>/$', views.upload_view, name='profile'),
    path(r'register/', views.register_view, name='register'),
    path(r'^login/$', login, {'template_name': 'account/login.html'}, name='login'),
    path(r'^logout/$', logout, {'template_name': 'home.html',
                                'next_page': '/login'}, name='logout'),
]
