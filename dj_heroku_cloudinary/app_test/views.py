from django.shortcuts import render, redirect

from dj_heroku_cloudinary.app_test.forms import ImageForm
from dj_heroku_cloudinary.app_test.models import Image


def image_upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_list')
    else:
        form = ImageForm()
    context = {
        'form': form
    }
    return render(request, 'app_test/image_upload.html', context)


def image_list(request):
    images = Image.objects.all()

    context = {
        'images': images,
    }

    return render(request, 'app_test/image_list.html', context)
