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
import requests


def image_view(request):
    if (os.path.join(settings.MEDIA_ROOT, 'images/Main_Img.jpg') == True):
        os.remove(os.path.join(settings.MEDIA_ROOT, 'images/Main_Img.jpg'))
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            if (os.path.join(settings.MEDIA_ROOT, 'images/Main_Img.jpg') == True):
                os.remove(os.path.join(settings.MEDIA_ROOT, 'images/Main_Img.jpg'))

            form.save()
            return redirect('index')
    else:
        form = ImageForm()
    return render(request, 'vision/image_upload.html', {'form': form})


def msft_vision(request):
    if (os.path.join(settings.MEDIA_ROOT, 'images/Main_Img.jpg') == True):
        os.remove(os.path.join(settings.MEDIA_ROOT, 'images/Main_Img.jpg'))
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            if (os.path.join(settings.MEDIA_ROOT, 'images/Main_Img.jpg') == True):
                os.remove(os.path.join(settings.MEDIA_ROOT, 'images/Main_Img.jpg'))

            form.save()
            return redirect('msft_index')
    else:
        form = ImageForm()
    return render(request, 'vision/msft_vision.html', {'form': form})


def msft_index(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'images/Main_Img.jpg' )
    image_data = open(file_path, "rb").read()
    url = "https://microsoft-azure-microsoft-computer-vision-v1.p.rapidapi.com/analyze"
    querystring = {"visualfeatures": "Tags"}

    headers = {
        'x-rapidapi-host': "microsoft-azure-microsoft-computer-vision-v1.p.rapidapi.com",
        'x-rapidapi-key': "6baec3a959msh19ecd967352bd8ap1d175ajsn23b072e115e0",
        'content-type': "application/octet-stream"
    }

    response = requests.request("POST", url, data=image_data, headers=headers, params=querystring)
    data_dict = response.json()
    predict=[]
    pred = data_dict['tags']
    x=0
    for ele in pred:
        name=ele['name']
        confidence = ele['confidence']
        predict.append("{}. {}: {:.2f}%".format(x + 1, name, confidence * 100))
        x += 1
    return render(request, 'vision/home.html', {'predict': predict})


def landing(request):
    predict = []
    return render(request, 'vision/landing.html', {'predict': predict})

def index(request):
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



