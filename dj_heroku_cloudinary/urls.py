from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from dj_heroku_cloudinary.app_test.views import image_upload, image_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', image_upload, name='image_upload'),
    path('images/', image_list, name='image_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
