#!/usr/bin/env python
# coding: utf-8

# # SD Map Visualization

# In[1]:


import os
import sys
import cv2
import numpy as np
import pandas as pd
import json


# In[2]:


sdmap = '/Users/akshaybharadwaj/Desktop/Personal_Projects/Kaggle/Mapless_Driving/OpenLane-V2/data/OpenLane-V2/OpenLane-V2_subset_A_sdmap/train/00000/sdmap.json'

with open(sdmap, 'r') as sd:
    map_json = json.load(sd)
#     print(map_json)


# In[3]:


len(map_json)


# In[4]:


# plot points
THICKNESS = 4

COLOR_DEFAULT = (0, 0, 255)
COLOR_DICT = {
    0:  COLOR_DEFAULT,
    1:  (255, 0, 0),
    2:  (0, 255, 0),
    3:  (255, 255, 0),
    4:  (255, 0, 255),
    5:  (0, 128, 128),
    6:  (0, 128, 0),
    7:  (128, 0, 0),
    8:  (128, 0, 128),
    9:  (128, 128, 0),
    10: (0, 0, 128),
    11: (64, 64, 64),
    12: (192, 192, 192),
}


# In[5]:


import matplotlib.pyplot as plt

# Function to draw lines on the image
def _draw_lane_centerline(points_list, color):
    for points in points_list:
        for i in range(len(points) - 1):
            x1 = int(points[i][0] + 1 * THICKNESS * 1.5)
            y1 = int(points[i][1] + 1 * THICKNESS * 1.5)
            x2 = int(points[i+1][0] + 1 * THICKNESS * 1.5)
            y2 = int(points[i+1][1] + 1 * THICKNESS * 1.5)
            # try:
            cv2.line(img_arr, pt1=(x1, y1), pt2=(x2, y2), color=color, thickness=THICKNESS, lineType=cv2.LINE_AA)
#         return image


# In[6]:


def visualization(road, sidewalk):
#     plt.figure(figsize=(12,8))
    
    if road is not None:
        _draw_lane_centerline(road, (0, 0, 255))
    
    if sidewalk is not None:
        _draw_lane_centerline(sidewalk, (255, 0, 0))


# In[7]:


import numpy as np
from PIL import Image

# Create a white image (RGB) with size 512x512
white_image = np.ones((2048, 2048, 3), dtype=np.uint8) * 255

# Convert to an image object and save
img_arr = np.array(Image.fromarray(white_image))
# img.show()


# In[8]:


road_list = []

for pt in map_json:
    if pt['category'] == 'road':
        road_list.append(pt['points'])


# In[14]:


sw_list = []

for pt in map_json:
    if pt['category'] == 'side_walk':
        sw_list.append(pt['points'])


# In[10]:


# visualization(road_list, None)


# In[16]:


visualization(None, sw_list)


# In[17]:


plt.imshow(img_arr)

