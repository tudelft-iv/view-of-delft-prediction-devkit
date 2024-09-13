# The View-of-Delft Prediction devkit
Welcome to the View-of-Delft Prediction (VoD-P) development kit. This repository contains the code and documentation associated with the VoD-P dataset.

![](https://www.vod.org/public/images/road.jpg)

## Overview
- [Introduction](#introduction)
- [Changelog](#changelog)
- [Devkit setup](#devkit-setup)
- [VoD-P](#vod-p)
  - [VoD-P setup](#vod-p-setup)
  - [Getting started with VoD-P](#getting-started-with-vod-p)
- [Known issues](#known-issues)
- [Citation](#citation)

## Introduction 
The View-of-Delft Prediction dataset is an extension of the [View-of-Delft dataset](https://github.com/tudelft-iv/view-of-delft-dataset/tree/main). It contains the 3D object annotations of the original dataset and additionally provides accurate 6-DoF global localisation and semantic map data.

The dataset is available in a format based on the [nuScenes dataset](https://www.nuscenes.org/), and hence this development kit is a modified version of the [nuScenes devkit](https://github.com/nutonomy/nuscenes-devkit).


## Changelog
[202-09-11] Released the View-of-Delft Prediction dataset and development kit.

## Devkit setup
The devkit is tested for Python >=3.6.
To install Python, please check [here](https://github.com/nutonomy/vod-devkit/blob/master/docs/installation.md#install-python).

TODO: Our devkit is available and can be installed via [pip](https://pip.pypa.io/en/stable/installing/) :
```
pip install vod-devkit
```


## VoD-P

### VoD-P setup
To download VoD-P, follow the instruction at the main [View-of-Delft dataset page](https://github.com/tudelft-iv/view-of-delft-dataset/tree/main#Access).
Download the zipfile when you receive the access link. 
Unzip the file and you should have the following folder structure:
```
/data/sets/vod
    maps	-	Folder for all map files (vectorized .json files).
    v1.0-*	-	JSON tables that include all the meta data and annotations. Each split (trainval, test) is provided in a separate folder.
```


### Getting started with VoD-P


## Known issues
N/A

## Citation
Please use the following citation when referencing the [View-of-Delft (VoD-P) dataset](https://ieeexplore.ieee.org/abstract/document/10493110):
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

The [View-of-Delft (VoD) dataset](https://ieeexplore.ieee.org/document/9699098) can be referenced using:
```
@ARTICLE{apalffy2022,
  author={Palffy, Andras and Pool, Ewoud and Baratam, Srimannarayana and Kooij, Julian F. P. and Gavrila, Dariu M.},
  journal={IEEE Robotics and Automation Letters}, 
  title={Multi-Class Road User Detection With 3+1D Radar in the View-of-Delft Dataset}, 
  year={2022},
  volume={7},
  number={2},
  pages={4961-4968},
  doi={10.1109/LRA.2022.3147324}}
```




