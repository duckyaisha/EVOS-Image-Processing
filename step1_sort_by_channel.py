#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 09:50:06 2025

@author: Alexander.Morano
"""

import os
import shutil
import glob

# Set your directory to wherever the images in question are
os.chdir('/Users/Alexander.Morano/Desktop/data/2024_12_19_GPCs_final_test/remnantplate/') 

# Set the prefix that precedes all images
prefix = 'rem_test'  # Replace this with your current prefix

# Step 1: List all TIF files matching the pattern
files = glob.glob(f"{prefix}_Plate_R_*.TIF")

# Step 2: Extract the channel label ('d0', 'd1', or 'd2') from the filenames
prefixes = set()
for file in files:
    prematch = file.split('.')[0]  #Extract the relevant part like 'd0', 'd1', 'd2'
    match = prematch[-2:]
  
    if match.startswith('d') and match[1] in '012':
        prefixes.add(match)

# Step 3: For each unique prefix, create a directory and move the matching files
for prefix_match in sorted(prefixes):
    
    # Create directory if it doesn't exist
    os.makedirs(prefix_match, exist_ok=True)
    
    # Move matching files into the respective directory
    for file in files:
        if prefix_match in file:
            shutil.move(file, os.path.join(prefix_match, os.path.basename(file)))

print("Files have been organized.")
