from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from helper import handle_upload
from photo_sharing.models import Photos
from datetime import datetime
import os


def home_view(request):
    if not request.user.is_authenticated:
        return redirect('users:login')
    context = {
        'title': 'Home',
        'user': request.user
    }
    return render(request, 'home.html', context=context)


def register_view(request):
    # POST, if the request.method==POST
    # Otherwise Its a GET request
    form = RegistrationForm(request.POST or None)
    # form is invalid if request.method == GET
    if form.is_valid():
        form.save()
        return redirect('users:login')

    args = {
        'form': form,
        'user': request.user
    }
    return render(request, 'register.html', args)


def profile_view(request, username):
    if not request.user.is_authenticated:
        return redirect('users:login')

    photos = Photos.objects.filter(username=request.user)
    user_profile = User.objects.filter(username=username).first()
    print('username:', username)
    context = {
        'title': 'Profile',
        'user': request.user,
        'same_user': True if request.user.username == username else False,
        'photos': photos,
        'full_name': user_profile.first_name + ' ' + user_profile.last_name
    }
    return render(request, 'profile.html', context=context)


def search_user(request):
    # u_name = request.POST['user_name']
    print('src:', request.POST)
    # if User.objects.filter(username=u_name).exists():
    #     return redirect('users:profile', username=u_name)
    return render(request, '404.html', context={'title': '404'})


def upload_photo(request):
    if not request.user.is_authenticated:
        return redirect('users:login')

    if request.method == 'POST' and request.FILES.get('photo'):
        time = '_' + str(datetime.now()).replace(' ', '_') + '_'
        print(time)
        file_name = request.user.username + time + \
                    str(request.FILES['photo']).replace(' ', '-')
        handle_upload(request.FILES['photo'], file_name)
        # User.objects.filter().exists()
        # file_name = os.path.join(settings.MEDIA_STORAGE, file_name)
        print('filename:', file_name)
        img = Photos.objects.create(username=request.user, photo_location=file_name)
        print('img:', img)
        return redirect('users:profile', username=request.user.username)

    context = {
        'title': 'Upload Photo',
        'user': request.user
    }
    return render(request, 'upload_photo.html', context=context)


def delete_photo(request, username, id):
    if request.user.username == username:
        img = Photos.objects.filter(id=id, username=request.user).first()
        if img:
            img.delete()
    return redirect('users:profile', username=request.user.username)



#
# < !-- < a
# href = "{% url 'profile' user.username %}" > < b > Profile < / b > < / a > -->
# < !-- < a
# href = "{% url 'logout' %}" > < b > Logout < / b > < / a > -->
