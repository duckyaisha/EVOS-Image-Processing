#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 17:29:36 2025

@author: Alexander.Morano
"""

import pandas as pd
import os
import shutil

root_path = '/Users/Alexander.Morano/Desktop/data/2025_01_16_NRXN1/R'

df = pd.read_csv("/Users/Alexander.Morano/Desktop/data/2025_01_16_NRXN1/R/results/finalresultsalpha.csv")

results_path = os.path.join(root_path, "results")
print(results_path)

for rownum, row in df.iterrows():
  # Get names
  subfolder_name = row['Subfolder']
  concentration = row['Concentration']
  antibody = row['Antibody']
  antigen = row['Antigen']
  
  ## Rename file in folder
  new_name = f"{antibody}_{concentration}_{antigen}"
  
  # Create the full path to the subfolder
  old_path = os.path.join(results_path, subfolder_name)
  new_path = os.path.join(results_path, new_name)
    
  # Step 4: Rename the folder
  if os.path.exists(old_path):
     os.rename(old_path, new_path)
     print(f"Renamed folder: {subfolder_name} -> {new_name}")
  else:
     print(f"Folder {subfolder_name} does not exist.")
     

#Next, let's sort into larger subfolders based on antibody name

#first: make a subfolder of "results" called "folders"
    
folders_path = os.path.join(root_path, "folders") 

#now we have the folders "folders" and "results" in the "R" directory.

os.mkdir(folders_path) 
print("Directory '%s' created" '%folders') 

unique_conditions = df['Antibody'].unique()

for condition in unique_conditions:
    
    dir_path = os.path.join(folders_path, condition)
    
    try:
        os.makedirs(dir_path, exist_ok=True)  # exist_ok=True prevents error if directory already exists
        print(f"Directory created: {dir_path}")
        
    except Exception as e:
        print(f"Error creating directory {condition}: {e}")
        


# Get the list of all folders in each directory
Results_Dirs = os.listdir(results_path)
Folders_Dirs = os.listdir(folders_path)

# Iterate over each folder in the first list
for folder in Results_Dirs:
    # Extract the first part of the folder name (before the first underscore)
    prefix = folder.split('_')[0]

    # Check if the prefix exists in the second list
    if prefix in Folders_Dirs:
        # Construct the full paths for the source and destination folders
        source_path = os.path.join(results_path, folder)
        destination_path = os.path.join(folders_path, prefix)

        # Move the folder into the corresponding folder in the second list
        try:
            # Ensure the destination folder exists
            if not os.path.exists(destination_path):
                print(f"Destination folder {destination_path} doesn't exist!")
            else:
                # Move the folder (it will merge into the second list folder)
                shutil.move(source_path, destination_path)
                print(f"Moved {folder} to {destination_path}")
                
        except Exception as e:
            print(f"Error moving {folder}: {e}")
    else:
        print(f"No matching folder found for {folder} in the second list")
        
#now let's move the graphs into there.
png_files = [f for f in os.listdir(results_path) if f.endswith('.png')]

# Iterate over each PNG file
for png_file in png_files:
    # Extract the prefix (name before the first underscore) from the PNG file name
    prefix = png_file.split('.png')[0]

    # Check if the prefix exists in the second list of folders
    if prefix in Folders_Dirs:
        # Construct the full paths for the source PNG file and the destination folder
        source_png_path = os.path.join(results_path, png_file)
        destination_folder_path = os.path.join(folders_path, prefix)

        # Move the PNG file into the corresponding folder in the second list
        try:
            # Ensure the destination folder exists
            if not os.path.exists(destination_folder_path):
                print(f"Destination folder {destination_folder_path} doesn't exist!")
            else:
                # Move the PNG file
                shutil.move(source_png_path, destination_folder_path)
                print(f"Moved {png_file} to {destination_folder_path}")
                
        except Exception as e:
            print(f"Error moving {png_file}: {e}")
    else:
        print(f"No matching folder found for {png_file} in the second list")
