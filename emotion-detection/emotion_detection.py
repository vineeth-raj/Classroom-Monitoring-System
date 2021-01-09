#!/usr/bin/env python
# coding: utf-8

# In[21]:


import torch
from torch import nn
import torchvision
from BlazeFace_PyTorch import blazeface

gpu = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
net = blazeface.BlazeFace().to(gpu)
net.load_weights("BlazeFace_PyTorch/blazeface.pth")
net.load_anchors("BlazeFace_PyTorch/anchors.npy")


# In[39]:


import cv2
import matplotlib.pyplot as plt
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')

video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    #cv2.imshow('Video', frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #frame = cv2.resize(frame, (128, 128))

    '''faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)'''

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything is done, release the capture
frame = cv2.resize(frame, (128, 128))
detections = net.predict_on_image(frame)
detections = detections.cpu().numpy()
for i in range(detections.shape[0]):
    ymin = int(detections[0, 0] * frame.shape[0])
    xmin = int(detections[0, 1] * frame.shape[1])
    ymax = int(detections[0, 2] * frame.shape[0])
    xmax = int(detections[0, 3] * frame.shape[1])
    face = frame[xmin:xmax, ymin:ymax]
    face = cv2.flip(face, 1)
    face = cv2.resize(face, (128, 128))
    sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    faces = cv2.filter2D(face, -1, sharpen_kernel)
    cv2.imwrite('images/{}.jpg'.format(i+1), faces)
    plt.imshow(faces)
video_capture.release()
cv2.destroyAllWindows()
#plt.show()


# In[17]:


get_ipython().system('python visualize.py')


# In[18]:


detections.shape


# In[19]:


detections.ndim


# In[20]:


detections.shape[0]


# In[ ]:




