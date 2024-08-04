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
- [Contributing](#contributing)
- [License](#license)

## Introduction

Autonomous driving systems rely on various perception modules to understand the environment around the vehicle. This repository provides a hands-on approach to learning and experimenting with some of these modules using Jupyter notebooks. The modules covered are:

- **Lane Line Detection**: Detecting the lane markings on the road.
- **Depth Estimation**: Estimating the distance of objects from the camera.
- **Bird's Eye View Representation**: Transforming the camera view to a top-down view for better spatial understanding.

## Installation

To run the notebooks in this repository, you need to have Python and Jupyter Notebook installed. You can install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

## Notebooks
### Lane Line Detection
This notebook demonstrates how to detect lane lines on the road using computer vision techniques. It covers preprocessing steps, edge detection, and applying a Hough Transform to identify lane lines.

Notebook: lane_line_detection.ipynb

### Depth Estimation
This notebook explores depth estimation using stereo vision and monocular depth estimation methods. It includes both traditional computer vision approaches and deep learning-based models.

Notebook: depth_estimation.ipynb

### Bird's Eye View Representation
This notebook shows how to transform the camera view to a bird's eye view (top-down perspective) to get a better understanding of the vehicle's surroundings. This transformation is useful for path planning and obstacle detection.

Notebook: birds_eye_view_representation.ipynb


