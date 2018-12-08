from django.http import HttpResponse
from django.shortcuts import render, redirect
from helper import handle_upload


def home_view(request):
    if request.method == request.GET:
        # TODO show uploaded photos
        pass
    else:
        # TODO upload photos
        pass


def upload_view(request):
    if request.method == 'POST' and request.FILES['photo']:
        handle_upload(request.FILES['photo'], str(request.FILES['photo']))
        return HttpResponse("Successful")
    return render(request, 'upload_file.html', context={})

