#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 09:51:19 2025

@author: Alexander.Morano
"""
#The reason we need to do this is because the FIJI macro requires the ZIP files that are the output of the CellPose function 
#to have the same name as the .TIFs on which the macro is run. 
#thus, we need to change the first part of the name of the d2 files (the red antibody channel) to d0_rois to match

import os

fileLocation = "/Users/Alexander.Morano/Desktop/data/2024_12_19_GPCs_final_test/titration/d2/"
fileList = os.listdir(fileLocation)
print(fileList)

for ii in fileList:
    newName = ii.replace('d2','d0_rois')
    if newName != ii:
        os.rename(fileLocation+ii,fileLocation+newName)
print(fileList)
