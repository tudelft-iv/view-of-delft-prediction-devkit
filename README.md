# The View-of-Delft Prediction devkit
Welcome to the View-of-Delft Prediction (VoD-P) development kit. This repository contains the code and documentation associated with the VoD-P dataset.

![](TODO)

## Overview
- [Introduction](#introduction)
- [Changelog](#changelog)
- [Devkit setup](#devkit-setup)
- [VoD-P](#vod-p)
  - [VoD-P setup](#vod-p-setup)
  - [Getting started with VoD-P](#getting-started-with-vod-p)
  - [Submitting to the VoD-P leaderboard](#submitting-to-the-vod-p-leaderboard)
- [Citation](#citation)

## Introduction 
The View-of-Delft Prediction dataset is an extension of the [View-of-Delft dataset](https://intelligent-vehicles.org/datasets/view-of-delft/). It contains the 3D object annotations of the original dataset and additionally provides accurate 6-DoF global localisation and semantic map data.

The dataset is available in a format based on the [nuScenes dataset](https://www.nuscenes.org/), and hence this development kit is a modified version of the [nuScenes devkit](https://github.com/nutonomy/nuscenes-devkit).


## Changelog
- [2024-11-15] Released a version of the development kit for Python 3.8.
- [2024-09-11] Released the View-of-Delft Prediction dataset and development kit.

## Devkit setup
The devkit is tested for Python 3.8. For a version of the devkit that is compatible with Python 3.6 and 3.7, see the v1.0.1 [PyPI release](https://pypi.org/project/vod-devkit/1.0.1/) or [tag](https://github.com/tudelft-iv/view-of-delft-prediction-devkit/releases/tag/v1.0.1). 
To install Python, please check [here](https://github.com/tudelft-iv/vod-devkit/blob/master/docs/installation.md#install-python).

Our devkit is available and can be installed via [pip](https://pip.pypa.io/en/stable/installing/):
```
pip install vod-devkit
```

For an advanced installation, see [installation](docs/installation.md) for detailed instructions.


## VoD-P

### VoD-P setup
To download VoD-P, follow the instructions at the main [View-of-Delft dataset page](https://intelligent-vehicles.org/datasets/view-of-delft/).
Download the zipfile when you receive the access link. 
Unzip the file and you should have the following folder structure:
```
/data/sets/vod
    maps	-	Folder for all map files (vectorized .json files).
    v1.0-*	-	JSON tables that include all the meta data and annotations. Each split (trainval, test) is provided in a separate folder.
```


### Getting started with VoD-P

Please follow these steps to make yourself familiar with the VoD dataset:
- Read the [main dataset page](https://intelligent-vehicles.org/datasets/view-of-delft/).
- [Request access](https://docs.google.com/forms/d/e/1FAIpQLSdKvkuKbzmJTn8raJBAWgekAJCpaQLS_ED63sUS89Ezo61RCQ/viewform) to the dataset.
- Download the dataset.
- Get the [vod-devkit code](https://github.com/tudelft-iv/vod-devkit/tree/main).
- Read the [tutorials](https://github.com/tudelft-iv/vod-devkit/tree/main/tutorials) or run one yourself using:
```
jupyter notebook $HOME/vod-devkit/tutorials/vod_tutorial.ipynb
```
- Read the View-of-Delft Prediction [paper](https://ieeexplore.ieee.org/document/10493110) for a closer look at the dataset.
- See the [FAQs](https://github.com/tudelft-iv/view-of-delft-prediction-devkit/blob/main/docs/faqs.md).


### Submitting to the VoD-P leaderboard

The VoD-P benchmark leaderboard can be found at TODO.

See the [benchmark instructions](https://github.com/tudelft-iv/view-of-delft-prediction-devkit/blob/main/docs/benchmark_instructions.md) for the submission format and rules.


## Citation
Please use the following citation when referencing the View-of-Delft (VoD-P) dataset:
```
@article{boekema2024vodp,
  author={Boekema, Hidde J-H. and Martens, Bruno K.W. and Kooij, Julian F.P. and Gavrila, Dariu M.},
  journal={IEEE Robotics and Automation Letters}, 
  title={Multi-class Trajectory Prediction in Urban Traffic using the View-of-Delft Prediction Dataset}, 
  year={2024},
  volume={9},
  number={5},
  pages={4806-4813},
  keywords={Trajectory;Roads;Annotations;Semantics;Pedestrians;Predictive models;History;Datasets for Human Motion;Data Sets for Robot Learning;Deep Learning Methods},
  doi={10.1109/LRA.2024.3385693}}

```


