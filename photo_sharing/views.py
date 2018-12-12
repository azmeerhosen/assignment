from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from helper import handle_upload
from photo_sharing.models import Photos
from datetime import datetime


def home_view(request):
    if not request.user.is_authenticated:
        return redirect('users:login')
    print('aaaaaaaaaaaaaaaaa')
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
    print("wejkfffffjjjjjjjjjjjjjjjjjjj")
    return render(request, 'register.html', args)


def profile_view(request, username):
    if not request.user.is_authenticated:
        return redirect('users:login')

    photos = Photos.objects.filter(username=request.user)
    user_profile = User.objects.filter(username=username)
    context = {
        'title': 'Profile',
        'user': request.user,
        'same_user': True if request.user.username == username else False,
        'photos': photos,
        'full_name': user_profile.first_name + ' ' + user_profile.last_name
    }
    return render(request, 'profile.html', context=context)


def upload_photo(request):
    if not request.user.is_authenticated:
        return redirect('users:login')

    if request.method == 'POST' and request.FILES['photo']:
        time = '_' + str(datetime.now()).replace(' ', '_') + '_'
        print(time)
        file_name = request.user.username + time + \
                    str(request.FILES['photo']).replace(' ', '-')
        handle_upload(request.FILES['photo'], file_name)
        # User.objects.filter().exists()
        ph = Photos.objects.create(username=request.user, photo_location=file_name)
        print(ph)
        return HttpResponse("Successful")

    context = {
        'title': 'Upload Photo',
        'user': request.user
    }
    return render(request, 'upload_photo.html', context=context)



#
# < !-- < a
# href = "{% url 'profile' user.username %}" > < b > Profile < / b > < / a > -->
# < !-- < a
# href = "{% url 'logout' %}" > < b > Logout < / b > < / a > -->
