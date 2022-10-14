# FaceDetectionModel
This repository represents a facedetection deeplearning model.
This model uses VGG 16 convolutional neural network to extract features. Extracted features were used for two problems:

  1) Classification problem: we have to recognize that there is a face on a small area of the screen. 
  2) Regression problem: we need to outline the area of the screen on which the found face is present. For that purpose we need to predict coordinates of a square that bounds founded face.

![alt text](https://github.com/IliaGamov/FaceDetectionModel/blob/main/readme_images/facedetection.PNG?raw=true)

Checkout MotionDetection.ipynb there are many comments and text sections that will describe pipeline in details.

# Installing

- git clone https://github.com/IliaGamov/FaceDetectionModel.git

- python = 3.9.7

- pip install -r requirements.txt

# Using pretrained model
model_deployed folder has a Webcam.py script that uses already trained model facetracker.h5, to run it yourself just use 

- python Webcam.py 

# Training
If you want to train this model yourself there is full pipeline inside MotionDetection.ipynb

To create dataset with your own images use make_photos.py script inside collect_images folder, that script uses your webcam and creates 90 images. Single photo is taken every 0.5s

After the photos have been taken, you need to create markup. For that purpose i used LabelMe, you should put labels inside data/labels/ 

In this repository there are some empty folders. It's purpose is to handle train/test/validation and augmentation train/test/validation images, so you can check if everything fine with your data during your preprocessing.



