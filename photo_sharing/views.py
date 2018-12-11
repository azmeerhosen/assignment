from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from helper import handle_upload
from photo_sharing.models import Photos


@login_required
def home_view(request):
    context = {
        'title': 'Home'
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


@login_required
def upload_view(request):
    if request.method == 'POST' and request.FILES['photo']:
        file_name = 'azmeer' + str(request.FILES['photo'])
        handle_upload(request.FILES['photo'], file_name)
        # User.objects.filter().exists()
        ph = Photos.objects.create(username=request.user, photo_location=file_name)
        print(ph)
        return HttpResponse("Successful")
    return render(request, 'upload_file.html', context={})

