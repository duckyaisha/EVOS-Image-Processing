#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 09:52:02 2025

@author: Alexander.Morano
"""
#Now we need to move the ZIP files that are the output of the CellPose process to the same subfolder as the antibody channel images on which we need to run our FIJI macro

import glob
import shutil

source_files = "/Users/Alexander.Morano/Desktop/data/2024_12_19_GPCs_final_test/titration/d0/*.zip"
target_folder = "/Users/Alexander.Morano/Desktop/data/2024_12_19_GPCs_final_test/titration/d2/"

# retrieve file list
filelist = glob.glob(source_files)
for single_file in filelist:
     # move file with full paths as shutil.move() parameters
    shutil.move(single_file,target_folder) 
