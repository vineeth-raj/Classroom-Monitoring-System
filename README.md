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

### Pose Estimation
Here we adapt multi-person pose estimation architecture to use it on edge devices.We follow the bottom-up approach from OpenPose because of its decent quality and robustness tonumber of people inside the frame. The networkmodel has4.1M parameters and 9 billions floating-point operations (GFLOPs) complexity,which is just∼15% of the baseline 2-stage OpenPose with almost the same quality. It detects a skeleton (which consists of keypoints and connections between them) to identify human poses for every person inside the image. The pose may contain up to 18 keypoints: ears, eyes, nose, neck, shoulders, elbows, wrists, hips, knees, and ankles.

![ScreenShot](https://github.com/vineeth-raj/Classroom-Monitoring-System/blob/main/Pose-Detection.png)

We profiled the code and removed extra memory allocations, parallelized keypoints extraction withOpenCV’s routine. This made code significantly faster, and the last bottleneck was the resize featuremaps to the input image size.We decided to skip the resize step and performed grouping directly on network output, but accuracydropped significantly. Thus step with upsampling feature maps cannot be avoided, but it is notnecessary to do it to input image size. Our experiments shown, that with upsample factor 8 theaccuracy is the same, as if resize to input image size. We used up-sample factor 4 for the demo purposes.
(inspired from this [paper](https://arxiv.org/pdf/1811.12004.pdf))

### Notes taker
In this we have done like simple audio to text converter using pyaudio and Halo.The written text was mailed to students as a notes.

## Procedure

- Firstly, the professor with the biometric device logs into his account  with his finger print and gets the attendance list of the subject he  handles for.
- Then the device is given to the students to keep their fingerprints and the attendance of that day is updated with the time of finger prints.
- The professor is kindly advised to keep the device on till his hourends  because assoonasthe professor logs in, the notes taker device will  start running and will stop if the biometric device stops.
- The notes taking device is connected tothecloudand will take  notes of the professor’s wordsandwillsend that to every student’s  webmail ID or mail ID once the professor logs out from his biometric  device(session over).
- This reduces the students effort of taking notes and make the  students listen more on the professors words.
- The professor can log out by placing his finger-print on the device the  second time.
- LCD display is kept on the biometric device to see the status whether the professor logged in or not and students fingerprint recognized or not.
- Meanwhile during the class, the emotion of the students is detected using their  facial expressions and the overall emotion of the students is displayed on the  smart-board(if available) every 3 seconds and will be sent as amessage to the  principal/the respective head and the teacher once the session ends.
- Various poses of the students are also detected in this process such as standing, raising hand, leaning on bench which can be used to know the interest of student over the subject.
- Considering the students privacy, we are not taking the student faces to a  server..hence we are processing the faces from the cameras inside the board using  OpenCV,blazeface-pytorch(used to detect face) and getting the emotions as output and this emotions are only going to the server and also the same for poses.

## Final Touch
We were able to create a system similar to the below pic. (inspired from this [website](https://edtechchina.medium.com/schools-using-facial-recognition-system-sparks-privacy-concerns-in-china-d4f706e5cfd0))

![](https://miro.medium.com/max/875/1*TqeG3GUeIOaXY36Dwu8rkA.jpeg)

- This can also be used in any public speaking platform to assess the emotion of audience and make it available to the speaker to make him deliver the speech better

## Future Scope

- This can be extended to automating the distribution of  corrected answer papers through server or in-fact  correction of answer papers can be automated or  automated invigilation.
- And also automatic on and off of lights and fans which  can used to reduce power wastage. The sweeper problem  can be solved by using the voice automated on and off.
- We can add recording facilities in the system so that  students can view the lectures whenever they wish to  watch.

## References

- https://medium.com/@EdtechChina/schools-using-facial-recognition-system-sparks-privacy-concerns-in-china-d4f706e5cfd0
- http://en.people.cn/n3/2018/0519/c90000-9461918.html

## Contributors
- [Shantosh](https://www.linkedin.com/in/shanthosh-kumar-921092174/)
