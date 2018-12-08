from django.urls import path
from photo_sharing import views


urlpatterns = [
    path(r'<id>/', views.upload_view, name='details'),
]
