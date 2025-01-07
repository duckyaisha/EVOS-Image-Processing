#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 09:53:33 2025

@author: Alexander.Morano
"""

import os
import shutil
import glob

os.chdir("/Users/Alexander.Morano/Desktop/data/2024_12_19_GPCs_final_test/remnantplate/results/") 

# Set your prefix
prefix = 'rem_test'  # Replace this with your current prefix

# Step 1: List all files matching the pattern
files = glob.glob(f"{prefix}_Plate_M_p00_0_*")

# Step 2: Extract the well name from this title.
prefixes = set()
for file in files:
    prematch = file.split('_')[6]
    
    match = prematch[:3]
    print(match)
  
    if match[0] in ('ABCDEFGH') and match[2] in '0123456789':
        prefixes.add(match)

# Step 3: For each unique prefix, create a directory and move the matching files
for prefix_match in sorted(prefixes):
    
    # Create directory if it doesn't exist
    os.makedirs(prefix_match, exist_ok=True)
    
    # Move matching files into the respective directory
    for file in files:
        if prefix_match in file:
            shutil.move(file, os.path.join(prefix_match, os.path.basename(file)))

print("Files have been organized AGAIN.")