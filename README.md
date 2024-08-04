# Autonomous Driving 

This repository contains Jupyter notebooks that demonstrate various perception modules used in autonomous driving systems, including lane line detection, depth estimation, and bird's eye view representation. Each module is implemented in a separate notebook and includes code, and visualizations.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Notebooks](#notebooks)
  - [Lane Line Detection](#lane-line-detection)
  - [Depth Estimation](#depth-estimation)
  - [Bird's Eye View Representation](#birds-eye-view-representation)
- [Usage](#usage)


## Introduction

Autonomous driving systems rely on various perception modules to understand the environment around the vehicle. This repository provides a hands-on approach to learning and experimenting with some of these modules using Jupyter notebooks. The modules covered are:

- **Lane Line Detection**: Detecting the lane markings on the road.
- **Depth Estimation**: Estimating the distance of objects from the camera.
- **Bird's Eye View Representation**: Transforming the camera view to a top-down view for better spatial understanding.

## Installation

### Using PIP
To run the notebooks in this repository, you need to have Python and Jupyter Notebook installed. You can install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

### Using Conda Environment
```
conda create --name autonomous-driving-env python=3.10
conda activate autonomous-driving-env
pip install -r requirements.txt
```

## Notebooks
### Lane Line Detection
This notebook demonstrates how to detect lane lines on the road using computer vision techniques. In this notebook we use transfer learning to train two state-of-the-art(SOTA) deep learning models like ResNet backbone model and  Vision Transformer model to detect lanelines in an image.

Notebook: Laneline Detection.ipynb

### Depth Estimation
This notebook explores depth estimation using monocular depth estimation methods. It uses the current SOTA depth estimation deep learning-based model - Depth AnythingV2 to obtain per pixel depth from an image. 

Notebook: Monocular_Depth_Estimation_Using_DepthAnythingV2.ipynb

### Bird's Eye View Representation
This notebook shows how to transform the camera view to a bird's eye view (top-down perspective) to get a better understanding of the vehicle's surroundings. This transformation is useful for path planning and Occupancy detection.

Notebook: BEV_transformation.ipynb


## Usage
1. Clone the repository:

```
git clone https://github.com/akshaybharadwaj11/Autonomous-Driving.git
cd Autonomous-Driving
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```



