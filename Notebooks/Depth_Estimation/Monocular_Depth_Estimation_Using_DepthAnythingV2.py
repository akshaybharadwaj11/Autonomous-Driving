import cv2
import torch
import matplotlib.pyplot as plt
import numpy as np
import time

from depth_anything_v2.dpt import DepthAnythingV2
import pandas as pd
 
data_dict_subset_A = pd.read_pickle('/work/cvpr/repo/OpenLane-V2/data/OpenLane-V2/data_dict_subset_A.pkl')
frame = data_dict_subset_A[('train', '00000', '315967376899927209')]

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

angles = frame['sensor'].keys()

for angle in angles:
    raw_img = cv2.imread("/work/cvpr/repo/OpenLane-V2/data/OpenLane-V2/data_files/" + frame['sensor'][angle]["image_path"])

    print("evaluating time")
    start_time = time.time()

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
    plt.savefig(f"angle_{angle}.png")
