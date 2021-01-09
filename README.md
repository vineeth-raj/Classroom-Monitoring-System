# Classroom-Monitoring-System
### Making the classroom smart using deep learning and Internet of Things

![ScreenShot](https://github.com/vineeth-raj/Classroom-Monitoring-System/blob/main/Classroom.png)

## Introduction
As a student, we feel like leaving the classroom, frustated due to boring lectures and we always wanted
the lecturer to know about our feelings.In olden era it is quite not possible, but in this deep learning
era we made it possible.Also it is very important to understand that the way lectures are delivered in
college or school is very important in shaping the career of students.Hence we came up with a solution
that can let the lecturer not only know about the students emotion but also he knows the gestures through
which he can make further moves.

## Objective
The main objectives of this system are:

- Make the attendance system flexible (biometric)
- Make the teachers and principal understand the interest of students on  the lectures by identifying their emotions and sitting postures.
- Automatic Notes taker.

## Components Required

### For Biometric Attendance:
- Arduino UNO Board(Atmega 328p Microcontroller)
- Fingerprint Sensor(R307 Module)
- LCD Display(16x2 LCD Module)
- Firebase(database to store students roll number)

### For Emotion and Posture Recognition
- Raspberry Pi
- Camera Module
- DeepLearning modules and models

### For Automatic Notes Taker
- Raspberry Pi4
- ReSpeaker USB MicArray

## Block Diagram of how our system works

![Screenshot](https://github.com/vineeth-raj/Classroom-Monitoring-System/blob/main/BlockDiagram-Classroom.png)

## Description

### Biometric Attendance
So we made a  fingerprint based biometric attendance system using Arduino.(inspired by [this](https://circuitdigest.com/microcontroller-projects/fingerprint-attendance-system-using-arduino-uno))

![ScreenShot](https://github.com/vineeth-raj/Classroom-Monitoring-System/blob/main/finger-print-sensor.png)

### Emotion Recognition

![ScreenShot](https://github.com/vineeth-raj/Classroom-Monitoring-System/blob/main/emotion-detection/images/results/Happy-Result.png)

![ScreenShot](https://github.com/vineeth-raj/Classroom-Monitoring-System/blob/main/emotion-detection/images/results/Neutral-Result.png)

First of all we detected faces from a camera using [BlazeFace-Torch](https://www.kaggle.com/humananalog/blazeface-pytorch) which is a lightweight framework.
Besides a bounding box, BlazeFace also predicts 6 keypoints for face landmarks (2x eyes, 2x ears, nose, mouth). Next using the face detected, we recognized the emotion of face among 7 emotions(Angry, Disgust, Fear, Happy, Sad, Surprise, Neutral) and then got the emoji for respective emotion. This recognition was done using VGG19 model which was trained on a million faces and was trained on Kaggle's GPU for 4 hours.

![](https://www.pyimagesearch.com/wp-content/uploads/2017/03/imagenet_vgg16.png)

![](https://www.researchgate.net/profile/Clifford_Yang/publication/325137356/figure/fig2/AS:670371271413777@1536840374533/llustration-of-the-network-architecture-of-VGG-19-model-conv-means-convolution-FC-means.jpg)
