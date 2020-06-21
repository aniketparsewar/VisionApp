from django.db import models
import os
from django.conf import settings

# Create your models here.

def path_and_rename(instance, filename):
    upload_to = 'images/'
    ext = 'jpg'
    instance.pk = 'Main_Img'
    # get filename
    filename = '{}.{}'.format(instance.pk, ext)
    #if (os.path.join(settings.MEDIA_ROOT, 'images/Main_Img.jpg') == True):
    try:
        os.remove(os.path.join(settings.MEDIA_ROOT, 'images/Main_Img.jpg'))
    except:
        pass

    # return the whole path to the file
    return os.path.join(upload_to, filename)

class ImageLens(models.Model):
    #name = models.CharField(default='Main_Img.jpg')
    Main_Img = models.ImageField(upload_to = path_and_rename)