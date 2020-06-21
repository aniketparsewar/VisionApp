# example of using a pre-trained model as a classifier
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.applications.vgg16 import VGG16
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import *
from django.conf import settings
import os


def image_view(request):
    if (os.path.join(settings.MEDIA_ROOT, 'images/Main_Img.jpg') == True):
        os.remove(os.path.join(settings.MEDIA_ROOT, 'images/Main_Img.jpg'))
    #print(request.method)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        #print(form.is_valid())
        if form.is_valid():
            if (os.path.join(settings.MEDIA_ROOT, 'images/Main_Img.jpg') == True):
                os.remove(os.path.join(settings.MEDIA_ROOT, 'images/Main_Img.jpg'))
            #document=form.save(commit=False)
            #document.name = 'Main_Img.jpg'
            #document.save()
            #print(document.name)
            form.save()
            return redirect('index')
    else:
        form = ImageForm()
    return render(request, 'vision/image_upload.html', {'form': form})

def index(request):

    # load an image from file
    file_path = os.path.join(settings.MEDIA_ROOT, 'images/Main_Img.jpg' )
    image = load_img(file_path, target_size=(224, 224))
    # convert the image pixels to a numpy array
    image = img_to_array(image)
    # reshape data for the model
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    # prepare the image for the VGG model
    image = preprocess_input(image)
    # load the model
    model = VGG16()
    # predict the probability across all output classes
    yhat = model.predict(image)
    # convert the probabilities to class labels
    label = decode_predictions(yhat)
    predict=[]
    for (i, (imagenetID, label, prob)) in enumerate(label[0]):
        #print("{}. {}: {:.2f}%".format(i + 1, label, prob * 100))
        predict.append("{}. {}: {:.2f}%".format(i + 1, label, prob * 100))
        #print(predict[i])
    # retrieve the most likely result, e.g. highest probability
    #label = label[0][0]
    #print(label
    # print the classification
    #print('%s (%.2f%%)' % (label[1], label[2] * 100))
    #predict = str(label[1]) + ', ' + str(label[2]*100) + '%'
    #print(predict)
    #ImageLens = ImageLens.objects.all()
    return render(request, 'vision/home.html', {'predict': predict})


def display_images(request):
    if request.method == 'GET':
        # getting all the objects of hotel.
        ImageLens = ImageLens.objects.all()
        return render((request, 'display_images.html',
                       {'main_images': ImageLens}))