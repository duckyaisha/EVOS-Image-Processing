#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 09:50:47 2025

@author: Alexander.Morano
"""

import numpy as np
import matplotlib.pyplot as plt
from cellpose import models, io, utils
from cellpose.io import imread
import os

modelpath = "/Users/Alexander.Morano/Desktop/cellpose_training/10x training/models/10X_NewCyto"
filepath = "/Users/Alexander.Morano/Desktop/data/2024_12_19_GPCs_final_test/remnantplate/d0/"

os.chdir(filepath)
files = os.listdir()
print(len(files))

model = models.CellposeModel(gpu = False, pretrained_model = modelpath)
channels = [[0,0]]

for i in files:
    image = io.imread(i)
    masks, flows, styles = model.eval(image, diameter = 60.0, channels = channels)
    io.save_rois(masks, i)