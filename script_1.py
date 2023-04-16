# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 08:30:26 2023

@author: Image903
"""
#%%

#simple frames
import cv2
import numpy as np
import os

video_frames = list()
cap = cv2.VideoCapture('vid.mp4')

if not os.path.exists('images'):
    os.makedirs('images')
index =0
while cap.isOpened():

    ret, frame = cap.read()

    if ret:
       # frame = cv2.resize(frame)
        video_frames.append(frame)
        name = './images/frame' + str(index) + '.jpg'
        print ('Creating...' + name)
        cv2.imwrite(name, frame)
        
        index +=1

    else:
        break


cap.release()
cv2.destroyAllWindows()

print(len(video_frames))
#%%
#%%

#subtract frames
import cv2
import numpy as np
import os

video_frames = list()
cap = cv2.VideoCapture('vid.mp4')

if not os.path.exists('images_d'):
    os.makedirs('images_d')
    
    
ret1, frame1 = cap.read() 
    
index =0
while cap.isOpened():

    ret2, frame2 = cap.read()

    if ret2:
       # frame = cv2.resize(frame)
        
        frame = frame1 - frame2
        video_frames.append(frame)
        name = './images_d/frame' + str(index) + '.jpg'
        print ('Creating...' + name)
        cv2.imwrite(name, frame)
        
        index +=1

    else:
        break
    
    frame1 = frame2


cap.release()
cv2.destroyAllWindows()

print(len(video_frames))




#%%

#subtract frames
import cv2
import numpy as np
import os

video_frames = list()
cap = cv2.VideoCapture('vid.mp4')

if not os.path.exists('images_abs'):
    os.makedirs('images_abs')
    
    
ret1, frame1 = cap.read() 
    
index =0
while cap.isOpened():

    ret2, frame2 = cap.read()

    if ret2:
       # frame = cv2.resize(frame)
        
        frame = cv2.absdiff(frame1 , frame2)
        video_frames.append(frame)
        name = './images_abs/frame' + str(index) + '.jpg'
        print ('Creating...' + name)
        cv2.imwrite(name, frame)
        
        index +=1

    else:
        break
    
    frame1 = frame2


cap.release()
cv2.destroyAllWindows()

print(len(video_frames))


#%%

#frames optical flow

import cv2
import numpy as np
import os

video_frames = list()
cap = cv2.VideoCapture('vid.mp4')

if not os.path.exists('images_o'):
    os.makedirs('images_o')
       
ret1, frame1 = cap.read()
prvs = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
hsv = np.zeros_like(frame1)
hsv[..., 1] = 255


if not cap.isOpened():
        print("Error opening video stream or file")
i = 0  
index =0
while cap.isOpened():

    ret2, frame2 = cap.read()

    if ret2:
       # frame = cv2.resize(frame)
        next = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        flow = cv2.calcOpticalFlowFarneback(prvs, next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
        mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
        hsv[..., 0] = ang * 180 / np.pi / 2
        hsv[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
        bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
        video_frames.append(bgr )
        name = './images_o/frame' + str(index) + '.jpg'
        print ('Creating...' + name)
        cv2.imwrite(name, bgr )
        
        index +=1

    else:
        break
    
    i += 1
    prvs = next



cap.release()
cv2.destroyAllWindows()

print(len(video_frames))

#%%

#skip frames
import cv2
import numpy as np
import os

video_frames = list()
video_reader = cv2.VideoCapture('vid.mp4')

SEQUENCE_LENGTH=20
# Get the total number of frames in the video.
video_frames_count = int(video_reader.get(cv2.CAP_PROP_FRAME_COUNT))

skip_frames_window = max(int(video_frames_count/SEQUENCE_LENGTH), 1)

if not os.path.exists('images_s'):
    os.makedirs('images_s')
index =0

for frame_counter in range(SEQUENCE_LENGTH):
            # Set the current frame position of the video.
            video_reader.set(cv2.CAP_PROP_POS_FRAMES, frame_counter * skip_frames_window)
        
            # Reading the frame from the video. 
            success, frame = video_reader.read() 
        
            # Check if Video frame is not successfully read then break the loop
            if not success:
                break
        
            # Resize the Frame to fixed height and width.
            #resized_frame = cv2.resize(frame, (IMAGE_HEIGHT, IMAGE_WIDTH))
            
            # Normalize the resized frame by dividing it with 255 so that each pixel value then lies between 0 and 1
            #normalized_frame = resized_frame / 255
            
            # Append the normalized frame into the frames list
            #video_frames.append(frame)
            video_frames.append(frame)
            name = './images_s/frame' + str(index) + '.jpg'
            print ('Creating...' + name)
            cv2.imwrite(name, frame)
            
            index +=1

cap.release()
cv2.destroyAllWindows()

print(len(video_frames))

#%%