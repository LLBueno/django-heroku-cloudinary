from django import forms
from dj_heroku_cloudinary.app_test.models import Image


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('description', 'image_file')
