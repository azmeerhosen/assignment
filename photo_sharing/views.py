from django.http import HttpResponse
from django.shortcuts import render
from helper import handle_upload
from photo_sharing.models import Photos


def home_view(request):
    if request.method == request.GET:
        # TODO show uploaded photos
        pass
    else:
        # TODO upload photos
        pass


def upload_view(request):
    if request.method == 'POST' and request.FILES['photo']:
        file_name = 'azmeer' + str(request.FILES['photo'])
        handle_upload(request.FILES['photo'], file_name)
        Photos.objects.create(username=request.user, photo_location=file_name)
        return HttpResponse("Successful")
    return render(request, 'upload_file.html', context={})

