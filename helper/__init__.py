import os

from django.conf import settings


def handle_upload(file, file_name):
    upload_path = settings.MEDIA_STORAGE
    if not os.path.exists(upload_path):
        os.mkdir('photos')

    with open(os.path.join(upload_path, file_name), 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
