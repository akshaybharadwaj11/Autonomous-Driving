import cv2
import torch
import matplotlib.pyplot as plt
import numpy as np
import time

from depth_anything_v2.dpt import DepthAnythingV2

model_configs = {
    'vits': {'encoder': 'vits', 'features': 64, 'out_channels': [48, 96, 192, 384]},
    'vitb': {'encoder': 'vitb', 'features': 128, 'out_channels': [96, 192, 384, 768]},
    'vitl': {'encoder': 'vitl', 'features': 256, 'out_channels': [256, 512, 1024, 1024]},
    'vitg': {'encoder': 'vitg', 'features': 384, 'out_channels': [1536, 1536, 1536, 1536]}
}

encoder = 'vitb' # or 'vits', 'vitb', 'vitg'

device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
print(device)

model = DepthAnythingV2(**model_configs[encoder])
model.to(device)


model.load_state_dict(torch.load(f'checkpoints/depth_anything_v2_{encoder}.pth', map_location='cpu'))
model.eval()

raw_img = cv2.imread("/work/cvpr/repo/OpenLane-V2/data/OpenLane-V2/data_files/train/00000/image/ring_front_center/315967376899927209.jpg")
start_time = time.time()
print("evaluating time")
depth = model.infer_image(raw_img) 
elapsed_time = time.time() - start_time
print(depth)

print(f"ETA : {elapsed_time}")
fig = plt.figure(figsize=(6, 3.2))

ax = fig.add_subplot(111)
ax.set_title('colorMap')
plt.imshow(depth)
ax.set_aspect('equal')

cax = fig.add_axes([0.12, 0.1, 0.78, 0.8])
cax.get_xaxis().set_visible(False)
cax.get_yaxis().set_visible(False)
cax.patch.set_alpha(0)
cax.set_frame_on(False)
plt.colorbar(orientation='vertical')
plt.savefig("abcd.png")
