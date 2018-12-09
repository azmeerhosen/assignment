from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from helper import handle_upload
from photo_sharing.models import Photos


def home_view(request):
    if request.method == request.GET:
        # TODO show uploaded photos
        pass
    else:
        # TODO upload photos
        pass


def register_view(request):
    # POST, if the request.method==POST
    # Otherwise None
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


def upload_view(request):
    if request.method == 'POST' and request.FILES['photo']:
        file_name = 'azmeer' + str(request.FILES['photo'])
        handle_upload(request.FILES['photo'], file_name)
        # User.objects.filter().exists()
        ph = Photos.objects.create(username=request.user, photo_location=file_name)
        print(ph)
        return HttpResponse("Successful")
    return render(request, 'upload_file.html', context={})

