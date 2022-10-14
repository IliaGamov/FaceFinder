# FaceDetectionModel
Facetracker script that uses deep learning for face finding.
# Installing

-git clone https://github.com/IliaGamov/FaceDetectionModel.git

-python = 3.9.7

-pip install -r requirements.txt

# Using pretrained model
model_deployed folder has a Webcam.py script that uses already trained model facetracker.h5, to run it yourself just use 

-python Webcam.py 

# Training
If you want to train this model yourself there is full pipeline inside MotionDetection.ipynb

To create dataset with your own images use make_photos.py script inside collect_images folder, that script uses your webcam and creates 90 images every 0.5s 

